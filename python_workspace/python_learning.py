from ctypes import cdll
dll = cdll.LoadLibrary('cmake_workspace/libdynamic_learning.dylib')
dll.qq()
