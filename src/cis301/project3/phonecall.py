from cis301.phonebill.abstract_phonecall import AbstractPhoneCall
from datetime import datetime

class PhoneCall(AbstractPhoneCall):
    def __init__(self, caller: str, callee: str, start_time: datetime, end_time: datetime):
        """
        Initializes a PhoneCall with the given caller, callee, start time, and end time.
        """
        self.caller = caller
        self.callee = callee
        self.start_time = start_time
        self.end_time = end_time

    def get_caller(self) -> str:
        """
        Returns the caller's phone number.
        """
        return self.caller

    def get_callee(self) -> str:
        """
        Returns the callee's phone number.
        """
        return self.callee

    def get_starttime(self) -> datetime:
        """
        Returns the start time as a datetime object.
        """
        return self.start_time

    def get_starttime_string(self) -> str:
        """
        Returns the start time as a string.
        """
        return self.start_time.strftime("%m/%d/%Y %H:%M")

    def get_endtime(self) -> datetime:
        """
        Returns the end time as a datetime object.
        """
        return self.end_time

    def get_endtime_string(self) -> str:
        """
        Returns the end time as a string.
        """
        return self.end_time.strftime("%m/%d/%Y %H:%M")

    def __str__(self) -> str:
        """
        Returns a string representation of the phone call.
        """
        return f"Phone call from {self.get_caller()} to {self.get_callee()} from {self.get_starttime_string()} to {self.get_endtime_string()}"