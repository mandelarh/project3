from cis301.project3.phonebill import PhoneBill
from cis301.project3.phonebill import PhoneBill
from cis301.project3.phonecall import PhoneCall
from cis301.project3.TextDumper import TextDumper
from cis301.project3 import phonebill, phonecall
from cis301.project3.TextParser import TextParser # Replace with your actual module name

# Test with your file
parser = TextParser("test.txt")
bill = parser.parse()

print(f"Customer: {bill.get_customer()}")
print("Calls:")
for call in bill.get_phonecalls():
    print(f"- {call.get_caller()} -> {call.get_callee()}")
    print(f"  Start: {call.get_starttime()}")
    print(f"  End:   {call.get_endtime()}")
'''
def test_text_dumper():
    # Create test bill
    bill = PhoneBill("Test Customer")

    # Add test calls (adjust based on your PhoneCall constructor)
    call1 = PhoneCall("555-111-1111", "555-222-2222", "01/01 12:00", "01/01 12:05")
    call2 = PhoneCall("555-333-3333", "555-444-4444", "01/01 13:00", "01/01 13:30")
    bill.add_phonecall(call1)
    bill.add_phonecall(call2)

    # Test dumping
    dumper = TextDumper("phonebills.txt")
    dumper.dump(bill)
    print("Test complete. Check test_output.txt")


if __name__ == "__main__":
    test_text_dumper()
'''