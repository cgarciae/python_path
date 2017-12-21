
import sys, os

class PythonPath(object):
    def __init__(self, base, relative = None, get_real_path = True, base_is_file = True):

        if get_real_path:
            base = os.path.realpath(base)

        if base_is_file:
            base = os.path.dirname(base)

        if relative:
            base = os.path.join(base, relative)

        self.dir_path = os.path.realpath(base)


    def __enter__(self):
        sys.path.insert(0, self.dir_path)
        return self.dir_path

    def __exit__(self, type, value, traceback):
        sys.path.remove(self.dir_path)