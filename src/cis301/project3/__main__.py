import sys
from cis301.project3.phonebill import PhoneBill
from cis301.project3.TextDumper import TextDumper
from cis301.project3.phonecall import PhoneCall
from cis301.project3.TextParser import TextParser
def create_phone_bill(customer_name: str):
    """
    Creates and returns a PhoneBill object.
    """
    from cis301.project3.phonebill import PhoneBill
    print("Creating PhoneBill object")
    return PhoneBill(customer_name)

def create_phone_call(caller: str, callee: str, start_time: str, end_time: str):
    """
    Creates and returns a PhoneCall object.
    """
    from cis301.project3.phonecall import PhoneCall
    #print('hey')
    return PhoneCall(caller, callee, start_time, end_time)

def add_phone_call_to_bill(bill, call):
    """
    Adds a PhoneCall to a PhoneBill.
    """
    #print('hey')
    bill.add_phonecall(call)
    print(bill)

def write(bill):
    file = "phonebills.txt"
    dumper = TextDumper(file)
    dumper.dump(bill)
    print(f"write complete. Check {file}")
def read(bill):
    parser = TextParser("phonebills.txt")
    bill = parser.parse()
    print(f"Customer: {bill.get_customer()}")
    print("Calls:")
    for call in bill.get_phonecalls():
        print(f"- {call.get_caller()} -> {call.get_callee()}")
        print(f"  Start: {call.get_starttime()}")
        print(f"  End:   {call.get_endtime()}")


def usage():
    help ='usage: project2 [options] <args> args are (in this order):\n'+\
        '\tcustomer\t\tPerson whose phone bill we’re modeling\n'+\
        '\tcallerNumber\t\tPhone number of caller\n'+\
        '\tcalleeNumber\t\tPhone number of person who was called\n'+\
        '\tstartTime\t\tDate and time call began (24-hour time)\n'+\
        '\tendTime\t\t\tDate and time call ended (24-hour time)\n'+\
        'options are (options may appear in any order):\n'+\
        '\t-print\t\t\tPrints a description of the new phone call\n'+\
        '\t-README\t\t\tPrints a README for this project and exits\n'+ \
        '\t-textfile file\t\t\tWhere to read/write the\n'+\
        'Date and time should be in the format: mm/dd/yyyy hh:mm'




def parse_cli_argv(argv):
    #check for options
    ##check for -README
    print_option = False
    readme_option = False
    index = 0
    if "-README" in argv and argv.index("-README")<2 :
        #poistion of Readme
        print(usage())
        return()
    elif "-README" in argv and argv.index("-README")> 1 :
        print(usage())
        return()
    else:
        pass
    if "-print" in argv:
        if argv.index("-print")!=0 :
            print(usage())
            return
        print_option = True
        print('print detected')
        index +=1
    if "-write" in argv:
        if print_option :
            if argv.index("-write")!=1 :
                print(usage())
                return
        else:
            if argv.index("-write")!=0:
                print(usage())
                return
        readme_option = True
        #print("Write option detected")
        index +=1

        if len(argv) < index +5:
            print(usage())
            return





    '''
    ## check for -print
    if "-print" in argv and argv.index("-print")==0:
        flag_printopt = True
        print("-print detected!")
    else:
        print(usage())
        return()

    if "-write" in argv:
        print("write detected!")
        index = 1
    '''


    customer = argv[index]
    caller = argv[index+1]
    callee = argv[index+2]
    start_time = argv[index+3]
    end_time = argv[index+4]

    bill = create_phone_bill(customer)
    call = create_phone_call(caller, callee, start_time, end_time)
    add_phone_call_to_bill(bill, call)
    if readme_option == True:
        select = input("type 'r' to read from file and 'w' to write to one")
        if select == 'w':
            write(bill)
        elif select == 'r':
            read(bill)
        else:
            print("Invalid input")
    if print_option == True:
        print(bill)
    #print(call)
    '''
    if "-write" in argv and argv.index("-write")==1:
        #print("-write detected!")
        write(bill)
    '''
def main(args=None):
        """
            This program that parses the command line, creates a
            Student, and prints a description of the student to
            standard out by invoking its toString method.
        """
        if args is None:
            args = sys.argv[1:]

        print(args)

        if not args:
            print(f">>> Project3. Missing command line arguments")
            return

        parse_cli_argv(args)

    # check number of arguments, we are expecting 7 args + options
'''
def usage():
    help ='usage: project2 [options] <args> args are (in this order):\n'+\
        '\tcustomer\t\tPerson whose phone bill we’re modeling\n'+\
        '\tcallerNumber\t\tPhone number of caller\n'+\
        '\tcalleeNumber\t\tPhone number of person who was called\n'+\
        '\tstartTime\t\tDate and time call began (24-hour time)\n'+\
        '\tendTime\t\t\tDate and time call ended (24-hour time)\n'+\
        'options are (options may appear in any order):\n'+\
        '\t-print\t\t\tPrints a description of the new phone call\n'+\
        '\t-README\t\t\tPrints a README for this project and exits\n'+ \
        '\t-textfile file\t\t\tWhere to read/write the\n'+\
        'Date and time should be in the format: mm/dd/yyyy hh:mm'

def create_phone_bill(customer_name: str):
    """
    Creates and returns a PhoneBill object.
    """
    from cis301.project3.phonebill import PhoneBill
    print("Creating PhoneBill object")
    return PhoneBill(customer_name)

def create_phone_call(caller: str, callee: str, start_time: str, end_time: str):
    """
    Creates and returns a PhoneCall object.
    """
    from cis301.project3.phonecall import PhoneCall
    print('hey')
    return PhoneCall(caller, callee, start_time, end_time)

def add_phone_call_to_bill(bill, call):
    """
    Adds a PhoneCall to a PhoneBill.
    """
    print('hey')
    bill.add_phonecall(call)
    print(bill)

def write(bill):
    dumper = TextDumper("phonebills.txt")
    dumper.dump(bill)
    print("Test complete. Check test_output.txt")

'''




if __name__ == "__main__":
    main()