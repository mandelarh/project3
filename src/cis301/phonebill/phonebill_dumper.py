import abc
from typing import TypeVar
from cis301.phonebill.abstract_phonebill import AbstractPhoneBill


class PhoneBillDumper (metaclass=abc.ABCMeta):

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
    def dump(bill: T):
        if not isinstance(bill, AbstractPhoneBill):
            raise Exception("Invalid object type. Expected type of AbstractPhoneBill")
        pass