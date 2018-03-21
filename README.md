# Python Path
`python_path` is a simple utility that lets you cleanly add routes to your `PYTHON_PATH`. Its very useful to safely load scripts from other folders.

## Installing
You can install `python_path` from pip
```
pip install python_path
```

## Usage
Lets do an example, image you have the following project structure

```
- main.py
- some_folder/
  - other.py 
```

Say we want to load `other.py` form `main.py`, since some_folder is not a submodule because it doesn't contain a `__init__.py` then we need to add `some_folder` to the `PYTHON_PATH`. To make this very easy we'll use `python_path` like this:

```python
from python_path import PythonPath

with PythonPath("some_folder"):
    import other
```
Here `some_folder` is added relative the `PWD`, if you are executing `main.py` from a different directory and still want to reference `some_folder`, then you should directly state relative to what file or folder the operations are being done:
```python
from python_path import PythonPath

with PythonPath("some_folder", relative_to = __file__):
    import other
```
In this example we used the path of the current file via the `__file__` property of the `main.py` module. In general `relative_to` can be a file or a folder, if its a file then the filename is remove when creating the final path. The previous is equivalent to:
```python
from python_path import PythonPath
import os

path = os.path.basename(__file__)
path = os.path.join(path, "some_folder")

with PythonPath(path):
    import other
```
