from abc import abstractmethod, ABC
from typing import TypeVar, List, final

from cis301.phonebill.abstract_phonecall import AbstractPhoneCall


class AbstractPhoneBill(ABC):
    """
     This abstract class represents a customer's phone bill that
     consists of multiple phone calls.
    """
    @abstractmethod
    def get_customer(self) -> str:
        """
            Returns:
                 the name of the customer whose phone bill this is
        """
        pass

    @abstractmethod
    def add_phonecall(self, phonecall):
        """
         Adds a phone call to this phone bill
        """
        pass

    T = TypeVar('T', bound=AbstractPhoneCall)
    @abstractmethod
    def get_phonecalls(self) -> List[T]:
        """
        Returns:
             all of the phone calls (as instances of AbstractPhoneCall) in this phone bill
        """

    @final
    def __str__(self) -> str:
        """
         Returns:
              a brief textual description of this phone bill
        """
        return self.get_customer() + "'s phone bill with " + len(self.get_phonecalls()) + " phone calls"

