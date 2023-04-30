# Introduction
Stitch fingerprint images together to create a single image with opencv and PySide6.

# Usage

Build executable program
``` bash
pip install pipenv
pipenv shell
pipenv install -r requirements.txt
pyi-makespec -F -w worksGUI.py
pyinstaller worksGUI.spec
```
Run
``` bash
pip install -r requirements.txt
python worksGUI.py
```