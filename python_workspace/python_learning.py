import os
import platform
from ctypes import cdll

dynamic_suffix = None
if platform.system().lower() == "darwin":
    dynamic_suffix = ".dylib"
elif platform.system().lower() == "linux":
    dynamic_suffix = ".so"

if not dynamic_suffix:
    print("platform system:%s is not supported!" % platform.system())
    exit(1)

if __name__ == "__main__":
    dynamic_library_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../lib")
    dll = cdll.LoadLibrary(os.path.join(dynamic_library_path, "libdynamic_learning" + dynamic_suffix))
    dll.qq()
