import pickle
from datetime import datetime
import pytest
from cis301.project3.phonebill import PhoneBill
from cis301.project3.phonecall import PhoneCall
from cis301.project3.__main__ import main, usage


class DataStore:

    @staticmethod
    def store(self, obj, fileName):
        file= None
        try:
            file = open(fileName, "wb")
            pickle.dump(obj, file)
        except:
            raise Exception("IO Exception")
        finally:
            if file != None:
                file.close();
    @staticmethod
    def load(self,fileName):
        obj=None
        try:
            file = open(fileName, "rb")
            obj = pickle.load(file)
        except:
            raise Exception("IO Exception")
        finally:
            return obj
class TestArgs:
    def test_README(self, capsys):
        args = ["-README", "-print", "Chris", "404-404-4444"]
        main(args)
        captured = capsys.readouterr()
        print(captured.out)
        assert str(usage()) == str(captured.out)

class TestPhoneBill:

    def test_main(self, capsys):
        print(main())
        captured = capsys.readouterr()
        config = DataStore.load("tdata.dat", "rb")
        assert config['usage'] == captured.out

    def test_phonebill(self):
        phonebill = PhoneBill("customer name")
        print(phonebill)

    @pytest.mark.parametrize('starttime',['1/15/2020 19:39', '1/15/2020 19:9'])
    @pytest.mark.parametrize('endtime', ['1/15/2020 19:39', '1/15/2020 19:9'])
    @pytest.mark.parametrize('phoneNum',['112-456-0000'])
    def test_phonecall(self,starttime, endtime, phoneNum):
        start_time = datetime.strptime(starttime, "%m/%d/%Y %H:%M")
        end_time = datetime.strptime(endtime, "%m/%d/%Y %H:%M")
        phonecall = PhoneCall(phoneNum, phoneNum, start_time, end_time)


    def test_addPhoneCall(self):
        phonebill = PhoneBill("Alex")
        start_time = datetime.strptime("1/15/2020 19:39" , "%m/%d/%Y %H:%M")
        end_time = datetime.strptime("01/15/2018 1:39", "%m/%d/%Y %H:%M")
        phonecall= PhoneCall("123-456-1031", "456-121-3333",start_time, end_time )
        phonebill.add_phonecall(phonecall)