# KM3NeT instrument response function

This project provides a versatile tool that can be used to quickly analyze the sensitivity of the **KM3NeT** detector for various source models.
Currently it considers only point-like sources. The main feature of the tool is deep targeting to ``gammapy`` software.


##  Installation

It is recommended to create an isolated *virtualenvironment* to not interfere
with other Python projects, preferably inside the project's folder.  
Create and activate a virtual environment:
```bash
  cd your_folder
  python3 -m venv venv
  . venv/bin/activate

  # then install package from pypi
  pip install -U pip
  pip install km3irf
```
