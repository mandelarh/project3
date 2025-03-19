import sys

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]

    print (args)
    parse_cli_argv(args)

    print(f">>> Project3. Missing command line arguments")

def parse_cli_argv(argv):

    #check for options
    ##check for -README
    if "-README" in argv and argv.index("-README")<2 :
        #poistion of Readme
        print(usage())
        return()
    elif "-README" in argv and argv.index("-README")> 1 :
        print(usage())
        return()
    else:
        pass

    ## check for -print
    if "-print" in argv and argv.index("-print")==0:
        flag_printopt = True
        print("-print detected!")
    else:
        print(usage())
        return()

    # check number of arguments, we are expecting 7 args + options

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


if __name__ == "__main__":
    main()