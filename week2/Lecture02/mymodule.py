# mymodule.py

__all__ = [ 'func', 'SomeClass' ] 

a = 37            # Not exported

def func():       # Exported 
    print(f'func says that a is {a}')

class SomeClass:  # Exported
    def method(self):
        print('method says hi')

print('loaded module')
