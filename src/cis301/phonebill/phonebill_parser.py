import abc
from typing import TypeVar
from cis301.phonebill.abstract_phonebill import AbstractPhoneBill


class PhoneBillParser (metaclass=abc.ABCMeta):
    """
    Classes that implement this interface read some source and from it create a phone bill.
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        """
        verifies if the implementing class has implemented all abstract methods
        """
        return (hasattr(subclass, 'dump') and
                callable(subclass.dump) or
                NotImplemented)

    T = TypeVar('T', bounds=AbstractPhoneBill)
    @abc.abstractmethod
    def parse(self)-> AbstractPhoneBill:
        """
        Parses some source and returns a phone bill

        Raises:
            raises I/O exception when accessing an invalid file
        """
        pass
