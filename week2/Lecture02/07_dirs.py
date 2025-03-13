import os
print(os.getcwd())

for x in os.listdir('.'):
    print(x)

print("------------------")

for x in os.listdir('files/'):
    print(x)

print("------------------")

# to find if the item is a file or directory
for x in os.listdir('.'):
    if os.path.isfile(x): print('f-', x)
    elif os.path.isdir(x): print('d-', x)
    elif os.path.islink(x): print('l-', x)
    else: print('---', x)

# recursive walk
for x in os.walk('.'):
    print(x)
