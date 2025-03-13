# shutil: for more details read:
# https://docs.python.org/3/library/shutil.html

import shutil
import os
source = os.listdir(".")
destination = "files/newdir/"
for files in source:
    print(files)
    if files.endswith(".txt"):
        shutil.copy(files, destination)


# globbing : another way to find out the contents of a directory

import glob
import os

CWD = os.getcwd()

for name in glob.glob(CWD+'/*'):
    print(name)

for name in glob.glob('*.py'):
    print(name)

# pickling

import pickle

emp = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}

# Write the data to a file using a context manager
with open("files/Emp.txt", "wb") as pickling_on:
    pickle.dump(emp, pickling_on)

# Read the data back using a context manager
with open("files/Emp.txt", "rb") as pickle_off:
    emp_loaded = pickle.load(pickle_off)

print(emp_loaded)
