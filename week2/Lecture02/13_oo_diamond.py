class A:
    def yow(self):
        print("A")

class B(A):
    def yow(self):
        print("B")

class C(A):
    def yow(self):
        print("C")

class D(B, C):
    pass

d = D()
d.yow() # which yow() method??

# Method resolution order
print(D.__mro__)
