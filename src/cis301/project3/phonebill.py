from cis301.phonebill.abstract_phonebill import AbstractPhoneBill
from cis301.phonebill.abstract_phonecall import AbstractPhoneCall
from typing import List

class PhoneBill(AbstractPhoneBill):
    def __init__(self, customer_name: str):
        """
        Initializes a PhoneBill with the given customer name.
        """
        self.customer_name = customer_name
        self.phonecalls = []  # List to store PhoneCall objects

    def get_customer(self) -> str:
        """
        Returns the name of the customer.
        """
        return self.customer_name

    def add_phonecall(self, phonecall: AbstractPhoneCall) -> None:
        """
        Adds a phone call to the bill.
        """
        self.phonecalls.append(phonecall)

    def get_phonecalls(self) -> List[AbstractPhoneCall]:
        """
        Returns all phone calls in the bill.
        """
        return self.phonecalls

    def __str__(self) -> str:
        """
        Provides a human-readable description of the phone bill.
        """
        return f"{self.get_customer()}'s phone bill with {len(self.get_phonecalls())} phone calls"