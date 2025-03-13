try:
    age = int(input("Please enter your age: "))
    print("I see that you are %d years old." % age)
except ValueError:
    print("Hey, that wasn't a number!")

"""
It is possible for one except clause to handle more than one kind of error: 
we can provide a tuple of exception types instead of a single type
"""

try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print("%d / %d = %f" % (dividend, divisor, dividend / divisor))
except(ValueError, ZeroDivisionError):
    print("Oops, something went wrong!")

# A try-except block can also have multiple except clauses

try:
    dividend = int(input("Please enter the dividend: "))
    divisor = int(input("Please enter the divisor: "))
    print("%d / %d = %f" % (dividend, divisor, dividend / divisor))
except ValueError:
    print("The divisor and dividend have to be numbers!")
except ZeroDivisionError:
    print("The divisor may not be zero!")