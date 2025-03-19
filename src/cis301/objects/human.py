from cis301.examples.mammal import Mammal
import inspect

class Human (Mammal):
    """
        This is a simple human class
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
    

    def says(self):
        return "Hello"



if __name__ == "__main__":
    h = Human("John")
    print(h)
    print(h.says())
    print(h.name)
    print(repr(h))
    print(type(h))
    print(type(h.giveMilk()))
    print(inspect.getmro(Human))