# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-12-04 19:39:03.679227 by PyXB version 1.2.4 using Python 2.7.3.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d218ecb4-7be4-11e4-bf46-20cf30e41ced')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 205, 16)
    _Documentation = None
STD_ANON._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON._CF_pattern.addPattern(pattern='[_a-zA-Z][_a-zA-Z0-9]*')
STD_ANON._InitializeFacetMap(STD_ANON._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 271, 16)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.input = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='input', tag='input')
STD_ANON_.output = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='output', tag='output')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 404, 20)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.ras = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ras', tag='ras')
STD_ANON_2.ijk = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='ijk', tag='ijk')
STD_ANON_2.lps = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='lps', tag='lps')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 434, 20)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.fiberbundle = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='fiberbundle', tag='fiberbundle')
STD_ANON_3.model = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='model', tag='model')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 478, 20)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.scalar = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='scalar', tag='scalar')
STD_ANON_4.label = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='label', tag='label')
STD_ANON_4.tensor = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='tensor', tag='tensor')
STD_ANON_4.diffusion_weighted = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='diffusion-weighted', tag='diffusion_weighted')
STD_ANON_4.vector = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='vector', tag='vector')
STD_ANON_4.model = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='model', tag='model')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: flagValueType
class flagValueType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flagValueType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 499, 4)
    _Documentation = None
flagValueType._CF_pattern = pyxb.binding.facets.CF_pattern()
flagValueType._CF_pattern.addPattern(pattern='-?[a-zA-Z]')
flagValueType._InitializeFacetMap(flagValueType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'flagValueType', flagValueType)

# Atomic simple type: longFlagValueType
class longFlagValueType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longFlagValueType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 531, 4)
    _Documentation = None
longFlagValueType._CF_pattern = pyxb.binding.facets.CF_pattern()
longFlagValueType._CF_pattern.addPattern(pattern='-?-?[_a-zA-Z][_a-zA-Z0-9]*')
longFlagValueType._InitializeFacetMap(longFlagValueType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'longFlagValueType', longFlagValueType)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """The root element for each module XML description. It must contain
                at least one "parameters" element.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 28, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__AbsentNamespace0_CTD_ANON_category', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 32, 16), )

    
    category = property(__category.value, __category.set, None, 'Classifies the module (e.g. Filtering, Segmentation).\n                            The value can be a dot separated string to create category hierarchies.\n                        ')

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_CTD_ANON_title', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 40, 16), )

    
    title = property(__title.value, __title.set, None, 'A human-readable name for the module.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_description', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 46, 16), )

    
    description = property(__description.value, __description.set, None, 'A detailed description of the modules purpose.')

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_version', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 52, 16), )

    
    version = property(__version.value, __version.set, None, 'The modules version number. A suggested format is:\n                            <p>\n                            major.minor.patch.build.status\n                            </p><p>\n                            where status is one of\n                            <ul>\n                            <li>vc: version controlled (pre-alpha), build can be a serial revision number, if any\n                            (like svn might have).</li>\n                            <li>a: alpha</li>\n                            <li>b: beta</li>\n                            <li>rc: release candidate</li>\n                            <li>fcs: first customer ship</li>\n                            </ul>\n                            </p>\n                        ')

    
    # Element documentation-url uses Python identifier documentation_url
    __documentation_url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'documentation-url'), 'documentation_url', '__AbsentNamespace0_CTD_ANON_documentation_url', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 72, 16), )

    
    documentation_url = property(__documentation_url.value, __documentation_url.set, None, 'A URL pointing to a documentation or home page of the module.\n                        ')

    
    # Element license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'license'), 'license', '__AbsentNamespace0_CTD_ANON_license', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 79, 16), )

    
    license = property(__license.value, __license.set, None, 'The type of license or a URL containing the license.')

    
    # Element contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'contributor'), 'contributor', '__AbsentNamespace0_CTD_ANON_contributor', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 85, 16), )

    
    contributor = property(__contributor.value, __contributor.set, None, 'The author(s) of the command line module.')

    
    # Element acknowledgements uses Python identifier acknowledgements
    __acknowledgements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'acknowledgements'), 'acknowledgements', '__AbsentNamespace0_CTD_ANON_acknowledgements', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 91, 16), )

    
    acknowledgements = property(__acknowledgements.value, __acknowledgements.set, None, 'Acknowledgements for funding agency, employer, colleague, etc.\n                        ')

    
    # Element parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'parameters'), 'parameters', '__AbsentNamespace0_CTD_ANON_parameters', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 99, 16), )

    
    parameters = property(__parameters.value, __parameters.set, None, 'Starts a group of parameters.')

    _ElementMap.update({
        __category.name() : __category,
        __title.name() : __title,
        __description.name() : __description,
        __version.name() : __version,
        __documentation_url.name() : __documentation_url,
        __license.name() : __license,
        __contributor.name() : __contributor,
        __acknowledgements.name() : __acknowledgements,
        __parameters.name() : __parameters
    })
    _AttributeMap.update({
        
    })



# Complex type parameters with content type ELEMENT_ONLY
class parameters (pyxb.binding.basis.complexTypeDefinition):
    """Starts a group of parameters."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'parameters')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__AbsentNamespace0_parameters_label', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 121, 12), )

    
    label = property(__label.value, __label.set, None, 'A short string used as the label for this group.')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_parameters_description', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 127, 12), )

    
    description = property(__description.value, __description.set, None, 'A description of this parameter group.')

    
    # Element boolean uses Python identifier boolean
    __boolean = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'boolean'), 'boolean', '__AbsentNamespace0_parameters_boolean', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 137, 16), )

    
    boolean = property(__boolean.value, __boolean.set, None, None)

    
    # Element integer uses Python identifier integer
    __integer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'integer'), 'integer', '__AbsentNamespace0_parameters_integer', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 139, 16), )

    
    integer = property(__integer.value, __integer.set, None, None)

    
    # Element float uses Python identifier float
    __float = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'float'), 'float', '__AbsentNamespace0_parameters_float', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 140, 16), )

    
    float = property(__float.value, __float.set, None, None)

    
    # Element double uses Python identifier double
    __double = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'double'), 'double', '__AbsentNamespace0_parameters_double', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 141, 16), )

    
    double = property(__double.value, __double.set, None, None)

    
    # Element string uses Python identifier string
    __string = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'string'), 'string', '__AbsentNamespace0_parameters_string', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 143, 16), )

    
    string = property(__string.value, __string.set, None, None)

    
    # Element directory uses Python identifier directory
    __directory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'directory'), 'directory', '__AbsentNamespace0_parameters_directory', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 144, 16), )

    
    directory = property(__directory.value, __directory.set, None, None)

    
    # Element integer-vector uses Python identifier integer_vector
    __integer_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'integer-vector'), 'integer_vector', '__AbsentNamespace0_parameters_integer_vector', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 146, 16), )

    
    integer_vector = property(__integer_vector.value, __integer_vector.set, None, None)

    
    # Element float-vector uses Python identifier float_vector
    __float_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'float-vector'), 'float_vector', '__AbsentNamespace0_parameters_float_vector', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 147, 16), )

    
    float_vector = property(__float_vector.value, __float_vector.set, None, None)

    
    # Element double-vector uses Python identifier double_vector
    __double_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'double-vector'), 'double_vector', '__AbsentNamespace0_parameters_double_vector', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 148, 16), )

    
    double_vector = property(__double_vector.value, __double_vector.set, None, None)

    
    # Element string-vector uses Python identifier string_vector
    __string_vector = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'string-vector'), 'string_vector', '__AbsentNamespace0_parameters_string_vector', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 150, 16), )

    
    string_vector = property(__string_vector.value, __string_vector.set, None, None)

    
    # Element integer-enumeration uses Python identifier integer_enumeration
    __integer_enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'integer-enumeration'), 'integer_enumeration', '__AbsentNamespace0_parameters_integer_enumeration', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 152, 16), )

    
    integer_enumeration = property(__integer_enumeration.value, __integer_enumeration.set, None, None)

    
    # Element float-enumeration uses Python identifier float_enumeration
    __float_enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'float-enumeration'), 'float_enumeration', '__AbsentNamespace0_parameters_float_enumeration', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 153, 16), )

    
    float_enumeration = property(__float_enumeration.value, __float_enumeration.set, None, None)

    
    # Element double-enumeration uses Python identifier double_enumeration
    __double_enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'double-enumeration'), 'double_enumeration', '__AbsentNamespace0_parameters_double_enumeration', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 154, 16), )

    
    double_enumeration = property(__double_enumeration.value, __double_enumeration.set, None, None)

    
    # Element string-enumeration uses Python identifier string_enumeration
    __string_enumeration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'string-enumeration'), 'string_enumeration', '__AbsentNamespace0_parameters_string_enumeration', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 155, 16), )

    
    string_enumeration = property(__string_enumeration.value, __string_enumeration.set, None, None)

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'point'), 'point', '__AbsentNamespace0_parameters_point', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 158, 16), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__AbsentNamespace0_parameters_region', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 159, 16), )

    
    region = property(__region.value, __region.set, None, None)

    
    # Element file uses Python identifier file
    __file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_parameters_file', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 161, 16), )

    
    file = property(__file.value, __file.set, None, None)

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_parameters_image', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 162, 16), )

    
    image = property(__image.value, __image.set, None, None)

    
    # Element geometry uses Python identifier geometry
    __geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry'), 'geometry', '__AbsentNamespace0_parameters_geometry', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 163, 16), )

    
    geometry = property(__geometry.value, __geometry.set, None, None)

    
    # Attribute advanced uses Python identifier advanced
    __advanced = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'advanced'), 'advanced', '__AbsentNamespace0_parameters_advanced', pyxb.binding.datatypes.boolean, unicode_default='false')
    __advanced._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 176, 8)
    __advanced._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 176, 8)
    
    advanced = property(__advanced.value, __advanced.set, None, 'This value is usually used in GUI generators to decide\n                    if the parameters belonging to this group should be initially hidden to the user or not.\n                ')

    _ElementMap.update({
        __label.name() : __label,
        __description.name() : __description,
        __boolean.name() : __boolean,
        __integer.name() : __integer,
        __float.name() : __float,
        __double.name() : __double,
        __string.name() : __string,
        __directory.name() : __directory,
        __integer_vector.name() : __integer_vector,
        __float_vector.name() : __float_vector,
        __double_vector.name() : __double_vector,
        __string_vector.name() : __string_vector,
        __integer_enumeration.name() : __integer_enumeration,
        __float_enumeration.name() : __float_enumeration,
        __double_enumeration.name() : __double_enumeration,
        __string_enumeration.name() : __string_enumeration,
        __point.name() : __point,
        __region.name() : __region,
        __file.name() : __file,
        __image.name() : __image,
        __geometry.name() : __geometry
    })
    _AttributeMap.update({
        __advanced.name() : __advanced
    })
Namespace.addCategoryObject('typeBinding', 'parameters', parameters)


# Complex type paramType with content type ELEMENT_ONLY
class paramType (pyxb.binding.basis.complexTypeDefinition):
    """This type specifies elements common to all parameter types."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paramType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_paramType_name', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12), )

    
    name = property(__name.value, __name.set, None, 'The unique name (within this module) of the parameter. This is only used\n                        internally.\n                    ')

    
    # Element flag uses Python identifier flag
    __flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flag'), 'flag', '__AbsentNamespace0_paramType_flag', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20), )

    
    flag = property(__flag.value, __flag.set, None, None)

    
    # Element longflag uses Python identifier longflag
    __longflag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'longflag'), 'longflag', '__AbsentNamespace0_paramType_longflag', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20), )

    
    longflag = property(__longflag.value, __longflag.set, None, None)

    
    # Element index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_paramType_index', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16), )

    
    index = property(__index.value, __index.set, None, 'An integer starting at 0, that specifies a module argument that has no flags.\n                            The index value 1000 is reserved as a marker for output parameters (see the "channel"\n                            element) to indicate that\n                            this parameter is used to return results during the execution of this module and does not\n                            need to be set.\n                        ')

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_paramType_description', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12), )

    
    description = property(__description.value, __description.set, None, 'A brief description of the parameter.')

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'label'), 'label', '__AbsentNamespace0_paramType_label', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12), )

    
    label = property(__label.value, __label.set, None, 'A label for parameter.')

    
    # Element default uses Python identifier default
    __default = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default'), 'default', '__AbsentNamespace0_paramType_default', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12), )

    
    default = property(__default.value, __default.set, None, 'A default value for the parameter. The default must be a type that is compatible\n                        with the\n                        parameter type. The vector parameters are specified as comma separated values of the atomic\n                        parameter type.\n                    ')

    
    # Element channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'channel'), 'channel', '__AbsentNamespace0_paramType_channel', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12), )

    
    channel = property(__channel.value, __channel.set, None, 'Specifies whether the parameter is an input or output parameter. Output\n                        parameters can for\n                        example specify file paths where to write output data (e.g. using the "image" element) or they\n                        can represent\n                        "simple return parameters", indicated by providing an "index" of 1000. The current values of\n                        suche simple return\n                        parameters are not passed to the module during its execution. Rather, the module itself reports\n                        these parameter\n                        values during execution.\n                    ')

    
    # Attribute hidden uses Python identifier hidden
    __hidden = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hidden'), 'hidden', '__AbsentNamespace0_paramType_hidden', pyxb.binding.datatypes.boolean, unicode_default='false')
    __hidden._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 282, 8)
    __hidden._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 282, 8)
    
    hidden = property(__hidden.value, __hidden.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __flag.name() : __flag,
        __longflag.name() : __longflag,
        __index.name() : __index,
        __description.name() : __description,
        __label.name() : __label,
        __default.name() : __default,
        __channel.name() : __channel
    })
    _AttributeMap.update({
        __hidden.name() : __hidden
    })
Namespace.addCategoryObject('typeBinding', 'paramType', paramType)


# Complex type constraintsType with content type ELEMENT_ONLY
class constraintsType (pyxb.binding.basis.complexTypeDefinition):
    """Constraints on the allowed parameter value for scalar types and their vector variants.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'constraintsType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 565, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element minimum uses Python identifier minimum
    __minimum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'minimum'), 'minimum', '__AbsentNamespace0_constraintsType_minimum', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 571, 12), )

    
    minimum = property(__minimum.value, __minimum.set, None, 'The minimum allowed value for the parameter. If not specified, the minimum is the\n                        smallest\n                        possible value for the parameter type.\n                    ')

    
    # Element maximum uses Python identifier maximum
    __maximum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maximum'), 'maximum', '__AbsentNamespace0_constraintsType_maximum', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 579, 12), )

    
    maximum = property(__maximum.value, __maximum.set, None, 'The maximum allowed value for the parameter. If not specified, the maximum is the\n                        largest\n                        possible value for the parameter type.\n                    ')

    
    # Element step uses Python identifier step
    __step = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step'), 'step', '__AbsentNamespace0_constraintsType_step', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 587, 12), )

    
    step = property(__step.value, __step.set, None, 'The increment for the parameter.')

    _ElementMap.update({
        __minimum.name() : __minimum,
        __maximum.name() : __maximum,
        __step.name() : __step
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'constraintsType', constraintsType)


# Complex type scalarVectorType with content type ELEMENT_ONLY
class scalarVectorType (paramType):
    """This type represents vectors of integers, floats, and doubles and can contain
                constraints on the domain of valid values for the vector elements.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scalarVectorType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 291, 4)
    _ElementMap = paramType._ElementMap.copy()
    _AttributeMap = paramType._AttributeMap.copy()
    # Base type is paramType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Element constraints uses Python identifier constraints
    __constraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constraints'), 'constraints', '__AbsentNamespace0_scalarVectorType_constraints', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 300, 20), )

    
    constraints = property(__constraints.value, __constraints.set, None, None)

    
    # Attribute hidden inherited from paramType
    _ElementMap.update({
        __constraints.name() : __constraints
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'scalarVectorType', scalarVectorType)


# Complex type multipleType with content type ELEMENT_ONLY
class multipleType (paramType):
    """Parameters of this type are allowed to be passed multiple times with
                different values to the module if the attribute "multiple" is set to true. Note that if such
                a parameter has no flags, its values must be passed as the last arguments to the module.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'multipleType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 312, 4)
    _ElementMap = paramType._ElementMap.copy()
    _AttributeMap = paramType._AttributeMap.copy()
    # Base type is paramType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple uses Python identifier multiple
    __multiple = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'multiple'), 'multiple', '__AbsentNamespace0_multipleType_multiple', pyxb.binding.datatypes.boolean, unicode_default='false')
    __multiple._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 321, 16)
    __multiple._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 321, 16)
    
    multiple = property(__multiple.value, __multiple.set, None, 'Allows this parameter to occur multiple times.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __multiple.name() : __multiple
    })
Namespace.addCategoryObject('typeBinding', 'multipleType', multipleType)


# Complex type enumerationType with content type ELEMENT_ONLY
class enumerationType (paramType):
    """Restricts the valid parameter value to one and only one element out of
                a specified descrete set of values.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'enumerationType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 357, 4)
    _ElementMap = paramType._ElementMap.copy()
    _AttributeMap = paramType._AttributeMap.copy()
    # Base type is paramType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Element element uses Python identifier element
    __element = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'element'), 'element', '__AbsentNamespace0_enumerationType_element', True, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 366, 20), )

    
    element = property(__element.value, __element.set, None, 'Defines one possible enumeration value.')

    
    # Attribute hidden inherited from paramType
    _ElementMap.update({
        __element.name() : __element
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'enumerationType', enumerationType)


# Complex type flagType with content type SIMPLE
class flagType (pyxb.binding.basis.complexTypeDefinition):
    """A single character flag (e.g. "s", "W", etc.). Not required if "longFlag" is specified.
            """
    _TypeDefinition = flagValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flagType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 505, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is flagValueType
    
    # Attribute alias uses Python identifier alias
    __alias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alias'), 'alias', '__AbsentNamespace0_flagType_alias', pyxb.binding.datatypes.string)
    __alias._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 512, 16)
    __alias._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 512, 16)
    
    alias = property(__alias.value, __alias.set, None, 'A comma separated list of aliases. Can be used to provide different flags for\n                            the same parameter.\n                        ')

    
    # Attribute deprecatedalias uses Python identifier deprecatedalias
    __deprecatedalias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deprecatedalias'), 'deprecatedalias', '__AbsentNamespace0_flagType_deprecatedalias', pyxb.binding.datatypes.string)
    __deprecatedalias._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 519, 16)
    __deprecatedalias._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 519, 16)
    
    deprecatedalias = property(__deprecatedalias.value, __deprecatedalias.set, None, 'A comma separated list of deprecated aliases. When invoking a module with one\n                            of these aliases,\n                            the callee will be notified about the new preferred flag name.\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __alias.name() : __alias,
        __deprecatedalias.name() : __deprecatedalias
    })
Namespace.addCategoryObject('typeBinding', 'flagType', flagType)


# Complex type longFlagType with content type SIMPLE
class longFlagType (pyxb.binding.basis.complexTypeDefinition):
    """A multi-character flag (e.g. "spacing", "Watcher", etc.). Not required if "flag" is
                specified.
            """
    _TypeDefinition = longFlagValueType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'longFlagType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 537, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is longFlagValueType
    
    # Attribute alias uses Python identifier alias
    __alias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alias'), 'alias', '__AbsentNamespace0_longFlagType_alias', pyxb.binding.datatypes.string)
    __alias._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 545, 16)
    __alias._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 545, 16)
    
    alias = property(__alias.value, __alias.set, None, 'A comma separated list of aliases. Can be used to provide different long\n                            flags for the same parameter.\n                        ')

    
    # Attribute deprecatedalias uses Python identifier deprecatedalias
    __deprecatedalias = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deprecatedalias'), 'deprecatedalias', '__AbsentNamespace0_longFlagType_deprecatedalias', pyxb.binding.datatypes.string)
    __deprecatedalias._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 552, 16)
    __deprecatedalias._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 552, 16)
    
    deprecatedalias = property(__deprecatedalias.value, __deprecatedalias.set, None, 'A comma separated list of deprecated aliases. When invoking a module with one\n                            of these aliases,\n                            the callee will be notified about the new preferred long flag name.\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __alias.name() : __alias,
        __deprecatedalias.name() : __deprecatedalias
    })
Namespace.addCategoryObject('typeBinding', 'longFlagType', longFlagType)


# Complex type scalarType with content type ELEMENT_ONLY
class scalarType (multipleType):
    """This type represents integers, floats, and doubles and can contain
                constraints on the domain of valid values.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scalarType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 336, 4)
    _ElementMap = multipleType._ElementMap.copy()
    _AttributeMap = multipleType._AttributeMap.copy()
    # Base type is multipleType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Element constraints uses Python identifier constraints
    __constraints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'constraints'), 'constraints', '__AbsentNamespace0_scalarType_constraints', False, pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 345, 20), )

    
    constraints = property(__constraints.value, __constraints.set, None, None)

    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple inherited from multipleType
    _ElementMap.update({
        __constraints.name() : __constraints
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'scalarType', scalarType)


# Complex type pointType with content type ELEMENT_ONLY
class pointType (multipleType):
    """A parameter describing a point or region in 3D with a specified coordinate system.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pointType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 382, 4)
    _ElementMap = multipleType._ElementMap.copy()
    _AttributeMap = multipleType._AttributeMap.copy()
    # Base type is multipleType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple inherited from multipleType
    
    # Attribute coordinateSystem uses Python identifier coordinateSystem
    __coordinateSystem = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coordinateSystem'), 'coordinateSystem', '__AbsentNamespace0_pointType_coordinateSystem', STD_ANON_2)
    __coordinateSystem._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 389, 16)
    __coordinateSystem._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 389, 16)
    
    coordinateSystem = property(__coordinateSystem.value, __coordinateSystem.set, None, 'Specifies the coordinate system. If unspecified, the executing module is free\n                            to interpret the\n                            coordinates in the most appropriate way. For more information about the different systems,\n                            see\n                            <a href="http://www.slicer.org/slicerWiki/index.php/Coordinate_systems">Coordinate\n                            Systems</a>.\n                            <ul>\n                            <li><b>ras</b> (Right, Anterior, Superior) coordinate system.</li>\n                            <li><b>ijk</b> image coordinate system.</li>\n                            <li><b>lps</b> (Left, Posterior, Superior) coordinate system.</li>\n                            </ul>\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __coordinateSystem.name() : __coordinateSystem
    })
Namespace.addCategoryObject('typeBinding', 'pointType', pointType)


# Complex type geometryType with content type ELEMENT_ONLY
class geometryType (multipleType):
    """Complex type geometryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geometryType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 422, 4)
    _ElementMap = multipleType._ElementMap.copy()
    _AttributeMap = multipleType._AttributeMap.copy()
    # Base type is multipleType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple inherited from multipleType
    
    # Attribute fileExtensions uses Python identifier fileExtensions
    __fileExtensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fileExtensions'), 'fileExtensions', '__AbsentNamespace0_geometryType_fileExtensions', pyxb.binding.datatypes.string)
    __fileExtensions._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 425, 16)
    __fileExtensions._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 425, 16)
    
    fileExtensions = property(__fileExtensions.value, __fileExtensions.set, None, 'A comma separated list of allowed file extensions.')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_geometryType_type', STD_ANON_3)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 430, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 430, 16)
    
    type = property(__type.value, __type.set, None, 'Optionally specifies the allowed geometry type.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fileExtensions.name() : __fileExtensions,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'geometryType', geometryType)


# Complex type fileType with content type ELEMENT_ONLY
class fileType (multipleType):
    """Complex type fileType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 452, 4)
    _ElementMap = multipleType._ElementMap.copy()
    _AttributeMap = multipleType._AttributeMap.copy()
    # Base type is multipleType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple inherited from multipleType
    
    # Attribute fileExtensions uses Python identifier fileExtensions
    __fileExtensions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fileExtensions'), 'fileExtensions', '__AbsentNamespace0_fileType_fileExtensions', pyxb.binding.datatypes.string)
    __fileExtensions._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 455, 16)
    __fileExtensions._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 455, 16)
    
    fileExtensions = property(__fileExtensions.value, __fileExtensions.set, None, 'A comma separated list of allowed file extensions (e.g. "nrrd,mhd").\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __fileExtensions.name() : __fileExtensions
    })
Namespace.addCategoryObject('typeBinding', 'fileType', fileType)


# Complex type imageType with content type ELEMENT_ONLY
class imageType (fileType):
    """Complex type imageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'imageType')
    _XSDLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 471, 4)
    _ElementMap = fileType._ElementMap.copy()
    _AttributeMap = fileType._AttributeMap.copy()
    # Base type is fileType
    
    # Element name (name) inherited from paramType
    
    # Element flag (flag) inherited from paramType
    
    # Element longflag (longflag) inherited from paramType
    
    # Element index (index) inherited from paramType
    
    # Element description (description) inherited from paramType
    
    # Element label (label) inherited from paramType
    
    # Element default (default) inherited from paramType
    
    # Element channel (channel) inherited from paramType
    
    # Attribute hidden inherited from paramType
    
    # Attribute multiple inherited from multipleType
    
    # Attribute fileExtensions inherited from fileType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_imageType_type', STD_ANON_4)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 474, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 474, 16)
    
    type = property(__type.value, __type.set, None, 'Optionally specifies the allowed image type.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', 'imageType', imageType)


executable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'executable'), CTD_ANON, documentation='The root element for each module XML description. It must contain\n                at least one "parameters" element.\n            ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', executable.name().localName(), executable)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'category'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Classifies the module (e.g. Filtering, Segmentation).\n                            The value can be a dot separated string to create category hierarchies.\n                        ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 32, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='A human-readable name for the module.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 40, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='A detailed description of the modules purpose.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 46, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The modules version number. A suggested format is:\n                            <p>\n                            major.minor.patch.build.status\n                            </p><p>\n                            where status is one of\n                            <ul>\n                            <li>vc: version controlled (pre-alpha), build can be a serial revision number, if any\n                            (like svn might have).</li>\n                            <li>a: alpha</li>\n                            <li>b: beta</li>\n                            <li>rc: release candidate</li>\n                            <li>fcs: first customer ship</li>\n                            </ul>\n                            </p>\n                        ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 52, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'documentation-url'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='A URL pointing to a documentation or home page of the module.\n                        ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 72, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'license'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The type of license or a URL containing the license.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 79, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'contributor'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The author(s) of the command line module.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 85, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'acknowledgements'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Acknowledgements for funding agency, employer, colleague, etc.\n                        ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 91, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'parameters'), parameters, scope=CTD_ANON, documentation='Starts a group of parameters.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 99, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 32, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 52, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 72, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 79, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 85, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 91, 16))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'category')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 32, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 40, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 46, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 52, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'documentation-url')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 72, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'license')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 79, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'contributor')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 85, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'acknowledgements')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 91, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'parameters')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 99, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'label'), pyxb.binding.datatypes.string, scope=parameters, documentation='A short string used as the label for this group.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 121, 12)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=parameters, documentation='A description of this parameter group.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 127, 12)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'boolean'), paramType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 137, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'integer'), scalarType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 139, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'float'), scalarType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 140, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'double'), scalarType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 141, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'string'), multipleType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 143, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'directory'), multipleType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 144, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'integer-vector'), scalarVectorType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 146, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'float-vector'), scalarVectorType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 147, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'double-vector'), scalarVectorType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 148, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'string-vector'), paramType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 150, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'integer-enumeration'), enumerationType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 152, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'float-enumeration'), enumerationType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 153, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'double-enumeration'), enumerationType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 154, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'string-enumeration'), enumerationType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 155, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'point'), pointType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 158, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'region'), pointType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 159, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'file'), fileType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 161, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), imageType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 162, 16)))

parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry'), geometryType, scope=parameters, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 163, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 121, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 127, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'boolean')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 137, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'integer')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 139, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'float')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 140, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'double')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 141, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'string')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 143, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'directory')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 144, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'integer-vector')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 146, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'float-vector')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 147, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'double-vector')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 148, 16))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'string-vector')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 150, 16))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'integer-enumeration')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 152, 16))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'float-enumeration')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 153, 16))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'double-enumeration')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 154, 16))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'string-enumeration')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 155, 16))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'point')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 158, 16))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'region')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 159, 16))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'file')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 161, 16))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 162, 16))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parameters._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 163, 16))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
parameters._Automaton = _BuildAutomaton_()




paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), STD_ANON, scope=paramType, documentation='The unique name (within this module) of the parameter. This is only used\n                        internally.\n                    ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flag'), flagType, scope=paramType, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'longflag'), longFlagType, scope=paramType, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'index'), pyxb.binding.datatypes.nonNegativeInteger, scope=paramType, documentation='An integer starting at 0, that specifies a module argument that has no flags.\n                            The index value 1000 is reserved as a marker for output parameters (see the "channel"\n                            element) to indicate that\n                            this parameter is used to return results during the execution of this module and does not\n                            need to be set.\n                        ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=paramType, documentation='A brief description of the parameter.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'label'), pyxb.binding.datatypes.string, scope=paramType, documentation='A label for parameter.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default'), pyxb.binding.datatypes.string, scope=paramType, documentation='A default value for the parameter. The default must be a type that is compatible\n                        with the\n                        parameter type. The vector parameters are specified as comma separated values of the atomic\n                        parameter type.\n                    ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12)))

paramType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'channel'), STD_ANON_, scope=paramType, documentation='Specifies whether the parameter is an input or output parameter. Output\n                        parameters can for\n                        example specify file paths where to write output data (e.g. using the "image" element) or they\n                        can represent\n                        "simple return parameters", indicated by providing an "index" of 1000. The current values of\n                        suche simple return\n                        parameters are not passed to the module during its execution. Rather, the module itself reports\n                        these parameter\n                        values during execution.\n                    ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(paramType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
paramType._Automaton = _BuildAutomaton_2()




constraintsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'minimum'), pyxb.binding.datatypes.double, scope=constraintsType, documentation='The minimum allowed value for the parameter. If not specified, the minimum is the\n                        smallest\n                        possible value for the parameter type.\n                    ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 571, 12)))

constraintsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maximum'), pyxb.binding.datatypes.double, scope=constraintsType, documentation='The maximum allowed value for the parameter. If not specified, the maximum is the\n                        largest\n                        possible value for the parameter type.\n                    ', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 579, 12)))

constraintsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step'), pyxb.binding.datatypes.double, scope=constraintsType, documentation='The increment for the parameter.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 587, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 571, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(constraintsType._UseForTag(pyxb.namespace.ExpandedName(None, 'minimum')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 571, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 579, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(constraintsType._UseForTag(pyxb.namespace.ExpandedName(None, 'maximum')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 579, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(constraintsType._UseForTag(pyxb.namespace.ExpandedName(None, 'step')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 587, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 571, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 579, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 570, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
constraintsType._Automaton = _BuildAutomaton_3()




scalarVectorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constraints'), constraintsType, scope=scalarVectorType, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 300, 20)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 300, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(scalarVectorType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraints')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 300, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scalarVectorType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(multipleType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
multipleType._Automaton = _BuildAutomaton_8()




enumerationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'element'), pyxb.binding.datatypes.string, scope=enumerationType, documentation='Defines one possible enumeration value.', location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 366, 20)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(enumerationType._UseForTag(pyxb.namespace.ExpandedName(None, 'element')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 366, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
enumerationType._Automaton = _BuildAutomaton_9()




scalarType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'constraints'), constraintsType, scope=scalarType, location=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 345, 20)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 345, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(scalarType._UseForTag(pyxb.namespace.ExpandedName(None, 'constraints')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 345, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scalarType._Automaton = _BuildAutomaton_10()




def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pointType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pointType._Automaton = _BuildAutomaton_11()




def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(geometryType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
geometryType._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(fileType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
fileType._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 198, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'flag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 219, 20))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 220, 20))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'longflag')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 222, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'index')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 223, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 235, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'label')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 241, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'default')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 247, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(imageType._UseForTag(pyxb.namespace.ExpandedName(None, 'channel')), pyxb.utils.utility.Location('/homes/students/weigl/workspace1/mur-cli/src/ctkCmdLineModule.xsd', 257, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
imageType._Automaton = _BuildAutomaton_14()

