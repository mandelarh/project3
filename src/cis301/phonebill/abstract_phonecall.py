from abc import ABC, abstractmethod
from datetime import date
from typing import final


class AbstractPhoneCall(ABC):
    """
      This abstract class represents a phone call between a caller (the
      phone number of the person who originates the call) and callee (the
      phone number of the person whose receives the phone call).  Phone
      calls begin and end at given times.
    """
    @abstractmethod
    def get_caller(self) -> str:
        """
        Returns:
             the phone number of the person who originated this phone call
        """
        pass


    @abstractmethod
    def get_callee(self) -> str:
        """
            Returns:
                 the phone number of the person who received this phone call
        """
        pass

    @abstractmethod
    def get_starttime(self) -> date:
        """
            Returns:
                the time that this phone call was originated as a date object
        """
        pass


    @abstractmethod
    def get_starttime_string(self) -> str:
        """
            Returns:
                 a textual representation of the time that this phone call was oribinated
        """
        pass


    @abstractmethod
    def get_endtime(self)-> date:
        """
            Returns:
                the time that this phone call was completed as a date object
        """
        pass


    @abstractmethod
    def get_endtime_string(self)-> str:
        """
            Returns:
                 a textual representation of the time that this phone call was completed
        """
        pass



    @final
    def __str__(self)-> str:
        """
        Returns:
             a brief textual description of this phone call.
        """
        return \
            "Phone call from " + self.get_caller() +\
            " to " + self.get_callee() +\
            " from " + self.get_starttime_string() +\
            " to " + self.get_endtime_string();
