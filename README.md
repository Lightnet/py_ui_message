# py_ui_message

# License: MIT

# Created By: Lightnet

# Status:
 * Testing.
 
# Packages:
 * Python 3.11.4
 * NumPy 1.6.2
 * pyinstaller (exe build)
 * CPython (lib build)

# Information:
  This is just prototype. Note there example from the lesson on the sites by using the search engine.

  Trying to build universal tool for chat message. Or just portable message database.

  One reason is learning and build tool for local chat message development.

  Idea to build some sort of peer to peer and torrent to create data management and backup system for messages. Just an idea.

# Design:
  * Back up page auth for temp build
  * Render component for solid-js
  * Rest API http request

# Connection types:
 * websocket
 * tcp/udp

# Set up for development build and Virtual Environment:

pip3 is for python 3.x to handle package version match version.

```
pip3 install --user pipenv
```
## Create folder current dir:
```
.venv
```
If create .venv folder current project dir else by default C:\Users\<username>\.virtualenvs\<name>

## set current dir:
```
set PIPENV_VENV_IN_PROJECT=1
```
## install package:
```
pipenv install -r requirements.txt
```
Install packages in the text file.

```
pipenv install <package_name>
pipenv install <package_name>==version
```

# Save Packages:
```
pipenv run pip freeze > requirements.txt
```
Save what packages for needed to run application.


# Run shell:
```
pipenv shell
```
  Run sandbox mode.
```
python src/main.py
```
  Run application.
```
exit
```
  Quit shell

# build application lib:
```
python setup.py build_ext --inplace
```

# Build application bin:
```
pyinstaller --onefile --clean src/main.py
```
```
pyinstaller --onefile -w --clean src/main.py
```

# Refs:
 * https://docs.python.org/3/library/tkinter.html
 * https://github.com/theochem/python-cython-ci-example/tree/master
 * https://neurohackweek.github.io/cython-tutorial/02-compiling/
 * https://stackoverflow.com/questions/2581784/can-cython-compile-to-an-exe
 * https://stackoverflow.com/questions/5105482/compile-main-python-program-using-cython
 * https://nbari.com/pipenv-pyinstaller/
