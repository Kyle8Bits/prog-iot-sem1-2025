# import os
# import sys

# get the current working directory
# CWD = os.getcwd()
# add the current working directory to the module search path
# print(sys.path)
# sys.path.append(CWD)
# print(sys.path)

import mymodule

print(mymodule.a)
mymodule.func()
s = mymodule.SomeClass()
s.method()

# from mymodule import func   # func = sys.modules['mymodule'].func

# func()
# mymodule.func()

# from mymodule import *

# func()
# s = SomeClass()
# s.method()
# print(a)
