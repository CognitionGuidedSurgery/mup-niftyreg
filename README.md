# MSML User Repository for CLI (executables)

This repository is a kick-start template for getting CLI (CommandLineInterface) executables into the 
[Medical Simulation Markup Language](http://github.com/CognitionGuidedSurgery/msml).


     Author: Alexander Weigl <uiduw@student.kit.edu>
     Date: 2014-12-06
     Version: 0.2
     License: GPLv3

## Getting Started

1. Clone the latest version of this repository:

        $ git clone --depth 0 https://github.com/CognitionGuidedSurgery/mur-cli.git
   
2. Install dependencies:

        $ pip install --user path.py pyxb jinja2
    

3. Exclude `alphabet/`, `bin`, `py` from `.gitignore` file.

4. Add executable into `bin` by linking or copying.

5. Call `make.py`

        $ ./make.py

Optional for sharing your MUR:

5. Set a new origin with your `<user>` and `<repo>`:

        $ git remote set-url origin https://github.com/<user>/<repo>.git
        $ git commit && git push
