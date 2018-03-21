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
- my_project/
  - main.py
  - some_folder/
    - other.py
    - another_folder/
      - another.py
```

Say we want to load `other.py` form `main.py`, since some_folder is not a submodule because it doesn't contain a `__init__.py` then we need to add `some_folder` to the `PYTHON_PATH`. To make this very easy we'll use `python_path` like this:

```python
# my_project/main.py

from python_path import PythonPath

with PythonPath("some_folder"):
    import other
```
and execute the file like this:
```bash
cd my_project
python main.py
```
Here `some_folder` is added relative the `PWD` (`my_project`), if you are executing `main.py` from another directory and still want to reference `some_folder`, then you should directly state relative to what file or folder the operations are being done:
```python
# my_project/main.py

from python_path import PythonPath

with PythonPath("some_folder", relative_to = __file__):
    import other
```
The previous is equivalent to:
```python
# my_project/main.py

from python_path import PythonPath
import os

path = os.path.basename(__file__)
path = os.path.join(path, "some_folder")

with PythonPath(path):
    import other
```
Now we can also execute the script from any path and it sould still work e.g:
```bash
python my_project/main.py
```

Finally we can also navigate the folder structure by passing multiple parameters, so if we want to import `main.py` from `another.py` which is inside `another_folder` we could do it like this

```python
# my_project/some_folder/another_folder/another.py

from python_path import PythonPath

with PythonPath("..", "..", relative_to = __file__):
    import main
```
This is equivalent to
```python
# my_project/some_folder/another_folder/another.py

from python_path import PythonPath
import os

path = os.path.join("..", "..")

with PythonPath(path, relative_to = __file__):
    import main
```
