PVS Specification and Verification System
=========================================

[![Build Status](https://travis-ci.org/SRI-CSL/PVS.svg?branch=master)](https://travis-ci.org/SRI-CSL/PVS)

PVS is a verification system: that is, a specification language integrated with support tools and a theorem prover. It is intended to capture the state-of-the-art in mechanized formal methods and to be sufficiently rugged that it can be used for significant applications. PVS is a research prototype: it evolves and improves as we develop or apply new capabilities, and as the stress of real use exposes new requirements.

For documentation and pre-built binaries, please visit http://pvs.csl.sri.com/.


Source layout
-------------
Files:

* README           - this file
* pvs              - the shell script for invoking pvs
* pvsio-web        - the shell script for invoking the pvsio-web prototyping tool
* pvs.sty	   - the style file supporting LaTeX output
* pvs-tex.sub      - the default substitution file for generating LaTeX

Directories:
* Examples - some simple example specifications
* emacs    - Emacs files.
* wish     - Tcl/Tk files
* bin      - shell scripts and executables
* lib      - prelude, help files, and libraries
* pvsio-web  - PVSio-web prototyping tool and example prototypes
* javascript -  experimental javascript front-ends for PVS. See [javascript/README.md](javascript/README.md) for more info on how to run the tools.
