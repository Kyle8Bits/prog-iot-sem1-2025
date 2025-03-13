import os
print(os.getcwd())
# os.chdir("Lecture02")
# print(os.getcwd())

# read whole file
f = open("files/demofile.txt", "r")
print(f.read())
# Close opened file
f.close()

# use a context manager with the "with" statement to automatically handle opening and closing the file, even if an exception occurs.
with open("files/demofile.txt", "r") as f:
    print(f.read())

# read parts of it
with open("files/demofile.txt", "r") as f1:
    print(f1.read(20))

# write to a file, it is "a" mode and not "w"
with open("files/demofile.txt", "a") as f2:
    f2.write(" Quote by - Jeffrey Martin, HonorCode")

# create a new file
with open("files/myfile.txt", "x") as f3:
    f3.write("Hello, World!")

# seek 

# Open a file - r+: open for reading and writing
fo = open("files/foo.txt", "r+")
print("Name of the file: ", fo.name)

lines = fo.readlines()
print("Read line: %s" % (lines))

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

with open("files/foo.txt", "r+") as fo:
    for line in fo.readlines():
        #print(line)
        print(line, end='')
