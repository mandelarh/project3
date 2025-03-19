from abc import ABC, abstractmethod

class Animal(ABC):
    """ This class is the base class in our animal hierarchy.
    Each animal has a name and it makes a sound. """

    __slots__=['_name']

    def __init__(self):
        self._name= None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name=name

    @abstractmethod
    def says(self):
        pass

    def __str__(self):
        return f"{self.name} says {self.says()}"

