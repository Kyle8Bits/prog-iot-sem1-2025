"""
Exception handling gives us an alternative way to deal with error-prone situations in our code. 
Instead of performing more checks before we do something to make sure that an error 
will not occur, we just try to do it and if an error does occur we handle it. 
This can allow us to write simpler and more readable code.
"""

# with checks
n = None
while n is None:
    s = input("Please enter an integer: ")
    if s.lstrip('-').isdigit():
        n = int(s)
        print("%s is an integer." % s)
    else:
        print("%s is not an integer." % s)

# with exception handling
n = None
while n is None:
    try:
        s = input("Please enter an integer: ")
        n = int(s)
        print("%s is an integer." % s)
    except ValueError:
        print("%s is not an integer." % s)


"""
 None: The equivalent of the null keyword in Python is None. 
 Often you will want to perform an action that may or may not work.
 Using None is one way you can check the state of the action later. 
 None is object-oriented!
"""