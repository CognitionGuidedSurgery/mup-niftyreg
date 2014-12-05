from __future__ import print_function
# Copyright (C) 2014 Alexander Weigl
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Transfers CLI executables into an MSML-usable form.


"""

__author__ = 'Alexander Weigl <uiduw@student.kit.edu>'
__date__ = "2014-12-05"
__version__ = "0.2"


import argparse
import subprocess
import os
import os.path
import sys
import jinja2
from path import path

import binding

# region parameter conversion
class MsmlArgument(object):
    def __init__(self, **kwargs):
        self.name = None
        self.physcial = None
        self.logical = None
        self.default = None
        self.doc = None
        self.target = None

# maps CLI type to MSML types
TYPE_TABLE = {
    'b': 'bool',
    'boolean': 'bool',
    'double': 'double',
    'd': 'double',
    'string_vector': 'vector.string',
    'integer' : 'int',
    'p': 'vector.int', # point (2d/3d)s
}


def default_arg(obj):
    arg = MsmlArgument()
    arg.name = obj.name

    typ = None
    if obj.longflag and obj.longflag:
        typ = obj.longflag._complexTypeDefinition__content
    elif obj.flag:
        typ = obj.flag._complexTypeDefinition__content

    if typ in TYPE_TABLE:
        arg.physical = TYPE_TABLE[typ]
    elif typ is None:
        pass
    else:
        print("%s is not defined in the TYPE_TABLE" % typ, file=sys.stderr)
        arg.physical = typ


    arg.logical = ""

    if obj.default:
        arg.default = obj.default.replace('"', '').replace("'", '')

    arg.index = obj.index

    arg.doc = "%s\n\n%s" % (obj.label, obj.description)
    return arg


def _integer_enumeration(integer_enumeration):
    return default_arg(integer_enumeration)


def _integer_vector(integer_vector):
    return default_arg(integer_vector)


def _directory(directory):
    return default_arg(directory)


def _double(double):
    return default_arg(double)


def _double_enumeration(enum):
    return default_arg(enum)


def _double_vector(vec):
    return default_arg(vec)


def _file(fil):
    return default_arg(fil)


def _float(floot):
    return default_arg(floot)


def _float_enumeration(enum):
    return default_arg(enum)


def _float_vector(vec):
    return default_arg(vec)


def _geometry(geometry):
    return default_arg(geometry)


def _image(image):
    return default_arg(image)


def _point(point):
    return default_arg(point)


def _region(region):
    return default_arg(region)


def _string(string):
    return default_arg(string)


def _string_enumeration(enum):
    return default_arg(enum)


def _string_vector(vec):
    return default_arg(vec)


def _boolean(boolean):
    return default_arg(boolean)


def _integer(integer):
    return default_arg(integer)


# endregion
# region jinja
jinjaenv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


def indent(string, i):
    return string.strip().replace("\n", " " * i + "\n")


jinjaenv.globals["indent"] = indent

operator_template = jinjaenv.get_template("operator.jinja2")


# endregion

class CreateCLI(object):
    def __init__(self, cli_exec):
        self._executable = cli_exec
        self.name = path(self._executable).namebase

    def _get_xml(self):
        sp = subprocess.Popen(["--xml"], executable=self._executable, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,
                              shell=True)
        sp.wait()
        if sp.returncode == 0:
            return sp.stdout.read()
        else:
            raise BaseException("-xml not worked")

    def _get_cli_model(self):
        xml = self._get_xml()
        return binding.CreateFromDocument(xml)

    def do(self):
        model = self._get_cli_model()
        category = model.category
        title = model.title or self.name
        description = model.description
        license = model.license or "unknown"
        contributor = model.contributor

        self.outputs = list()
        self.parameters = list()
        self.inputs = list()

        defined_slots = []

        TYPES = (
            "boolean",
            "directory",
            "double",
            "double_enumeration",
            "double_vector",
            "float",
            "float_enumeration",
            "float_vector",
            "integer",
            "integer_enumeration",
            "integer_vector",
            "point",
            "region",
            "string",
            "string_enumeration",
            "string_vector",
            "file",
            "geometry",
            "image",
        )

        for ps in model.parameters:
            for t in TYPES:
                fn = "_%s" % t
                fn = globals()[fn]
                self.group(fn, getattr(ps, t))

                # self._directory(ps.double)
                # self._double(ps.double)
                # self._double_enumeration(ps.double_enumeration)
                # self._double_vector(ps.double_vector)
                # self._float(ps.float)
                # self._float_enumeration(ps.float_enumeration)
                # self._float_vector(ps.float_vector)
                # self._integer(ps.integer)
                # self._integer_enumeration(ps.integer_enumeration)
                # self._integer_vector(ps.integer_vector)
                # self._point(ps.point)
                # self._region(ps.region)
                # self._string(ps.string)
                # self._string_enumeration(ps.string_enumeration)
                # self._string_vector(ps.string_vector)
                # self._file(ps.file)
                # self._geometry(ps.geometry)
                # self._image(ps.image)

        return operator_template.render(
            name=self.name,
            documentation="",
            executable=self._executable,
            category=category,
            title=title,
            description=description,
            license=license,
            contributor=contributor,
            inputs=self.inputs,
            parameters=self.parameters,
            outputs=self.outputs
        )

    def group(self, fn, elements):
        for e in elements:
            arg = fn(e)

            if e.channel == "input":
                self.inputs.append(arg)
            elif e.channel == "output":
                self.outputs.append(arg)
            else:
                self.parameters.append(arg)


#region command line
def create_argument_parser():
    p = argparse.ArgumentParser()
    p.add_argument("executable", metavar="EXECUTABLE", nargs='*', help="CLI executable")
    p.add_argument("-o", "--output-dir", metavar="FOLDER", action="store", dest="output_dir", help="output folder",
                   default="alphabet/")
    return p


def main():
    args = create_argument_parser().parse_args()

    if not args.executable:
        binfolder = path("./bin/")
        print("ALL MODE ON, take every executable in %s" % binfolder.abspath())
        executables = filter(lambda fpath: os.access(fpath, os.X_OK),
                             binfolder.walkfiles("*",errors="ignore"))
    else:
        executables = args.executable

    for executable in executables:
        create = CreateCLI(executable)
        msml_xml = create.do()
        fil = "%s/%s.msml.xml" % (args.output_dir, create.name)
        print("Write %s to %s" % (executable, fil))
        with open(fil, 'w') as fp:
            fp.write(msml_xml)

#endregion