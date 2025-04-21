from cis301.phonebill.abstract_phonebill import AbstractPhoneBill
from cis301.phonebill.phonebill_dumper import PhoneBillDumper
from cis301.project3.phonebill import PhoneBill



class TextDumper(PhoneBillDumper):
    def __init__(self, output_file):
        self.output_file = output_file

    def dump(self, bill: AbstractPhoneBill):  # ← Renamed to 'bill' for consistency
        # Direct type checking (no super().dump() call)
        if not isinstance(bill, AbstractPhoneBill):
            raise TypeError("Expected AbstractPhoneBill.")

        with open(self.output_file, 'w') as f:
            f.write(f"Customer: {bill.get_customer()}\n")
            for call in bill.get_phonecalls():
                f.write(f"Call: {call.caller} → {call.callee}\n")  # ← Adjust attributes as needed