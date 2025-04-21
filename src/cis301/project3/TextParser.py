from cis301.phonebill.phonebill_parser import PhoneBillParser
from cis301.phonebill.abstract_phonebill import AbstractPhoneBill
from cis301.project3 import phonebill
from cis301.project3.phonebill import PhoneBill
from cis301.project3.phonecall import PhoneCall


class TextParser(PhoneBillParser):
    def __init__(self, input_file):
        self.input_file = input_file

    def parse(self) -> PhoneBill:
        with open(self.input_file, "r") as file:
            customer = file.readline().strip()
            customer = customer.replace("Customer: ", "")
            bill = phonebill.PhoneBill(customer)

            for line in file:
                if line:
                    parts = line.rstrip().split(" ")
                    caller = parts[0]
                    callee = parts[1]
                    start_time = f"{parts[2]} {parts[3]}"
                    end_time = f"{parts[4]} {parts[5]}"
                    call = PhoneCall(caller, callee, start_time, end_time)

                    bill.add_phonecall(call)
                else:
                    print('incorect format')
            return bill



