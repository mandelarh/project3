from cis301.objects.human import Human
import csv
import json
import yaml
import pickle
class Person(Human):
    def __init__(self, name, Phone, Email):
        super().__init__(name)
        self.phone = Phone
        self.email = Email
    def __str__(self):
        return f"name:{self.name}\t phone:{self.phone}\t email: {self.email}\n"
    
    def toCSV(self):
        return [self.name, self.phone, self.email]
    
    
    def __eq__(self, other):
        if self.name == other.name and \
        self.email == other.email and \
        self.phone == other.phone:
            return True
        else:
            return False
        
    def __lt__(self, other):
        return (self.name.lower() < other.name.lower())
    
    def toJ3son(self):

        return f'''{{
    "name": "{self.name}",
    "phone": "{self.phone}",
    "email": "{self.email}"
}}'''

    def toxml(self, filename):
        import xml.etree.ElementTree as ET
        root = ET.Element('person')
        ET.SubElement(root, 'name').text = self.name
        ET.SubElement(root, 'email').text = self.email
        ET.SubElement(root, 'phone').text = self.phone
        tree = ET.ElementTree(root)
        tree.write(filename)


    def fromxml(self, filename):
        import xml.etree.ElementTree as ET
        return (ET.parse(filename))

    
    @staticmethod
    def compare_by_email(p1,p2):
        if p1.email == p2.email:
            return 0
        elif p1.email < p2.email:
            return -1
        else:
            return 1
class phonebook:
    def __init__(self):
        self.contacts = [] 

    def add_contact(self, person):
        self.contacts.append(person)

    def del_contact(self, person):
        self.contacts.remove(person)

    def toCSV(self, filename):
        csv_data = []
        for contact in self.contacts:
            csv_data.append(contact.toCSV())
        
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'phone', 'email'])
            writer.writerows(csv_data)

    def fromCSV(self, filename):
        resultset = []
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            self.contacts.clear()
            next(reader) # skipping the first row thats used as a header 
            for row in reader:
                if len(row) > 0:
                    #resultset.append(row)
                    self.contacts.append(Person(row[0], row[1], row[2]))
                print(row)
            return resultset
    
    
    

    def toJ3SON(self, filename=None):
        phonebook_data = {
            "phonebook": [json.loads(contact.toJ3son()) for contact in self.contacts]
        }
        jsondata = json.dumps(phonebook_data, indent=4)  # Pretty-print JSON
    
        if filename:
            with open(filename, "w") as jsonfile:
                jsonfile.write(jsondata)
        return jsondata
    
    def phonebook_constructor_from_dict(self, dictdata):
        pb = phonebook()
        for contact in dictdata["phonebook"]:
            person = Person(contact["name"], contact["phone"], contact["email"])
            pb.add_contact(person)
        return pb

        
    
    def fromJ3son(self, filename):
        jsondata = ""
        with open(filename, "r") as jsonfile:
            jsondata = json.load(jsonfile)
            print(jsondata)
            pb = phonebook()
            return self.phonebook_constructor_from_dict(jsondata)
            '''
            for contact in jsondata["phonebook"]:
                person = Person(contact["name"], contact["phone"], contact["email"])
                pb.add_contact(person)
            return pb
            '''
    def toyaml(self, filename):
        with open(filename, "w") as yamlfile:
            yamldata = self.toJ3SON()
            yaml.dump(json.loads(yamldata), yamlfile)

    def fromyaml(self, filename):
        with open(filename, "r") as yamlfile:
            yamldata = yaml.safe_load(yamlfile)
            print(yamldata)
            return self.phonebook_constructor_from_dict(yamldata)
        

    def topickle(self,filename):
        with open(filename, "wb") as picklefile: # wb = write binary 
            pickle.dump(self, picklefile)

    def frompickle(self,filename):
        with open(filename, "rb") as picklefile: #rb = read binary
            return pickle.load(picklefile)

            

        
class util:
    @staticmethod

    def textfilewriter1(filename,data):
        file = open(filename, "w") 
        file.write("Data\n")
        file.write(data)
        file.close()

    def textfilewriter2(filename,data):
        #with open doesent require you to close file
        with open(filename, "a") as file: # a = append
            file.write("Data\n")
            file.write(data)
            file.close()

    def binfilewriter1(filename, data):
        with open(filename,"ab") as binfile: # a = append b = binary
            binfile.write(b"Data\n")
            binfile.write(data.encode()) #encode when using binary to convert string into bite array
    def textfilereader1(filename,data):
        with open(filename, "r") as file:
            return file.read()
    '''
    @staticmethod
    def csvfilewriter1(filename, data):
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'phone', 'email'])
            writer.writerrows()
    '''
        
    
    
    
    
    

    


    
    
if __name__ == '__main__':
    
    p1 = Person('mandela', '763-710-1431', 'mandela.haulcy@students.cau.edu')
    p2 = Person('wynton', '612-759-0233', 'ilovefood3901@gmail.com')
    '''
    if p1 == p2:
        print('its a match!')
    else:
        print('no match found')
    '''
    util.textfilewriter1("textfile1.txt1","heres some data") 
    util.textfilewriter2("textfile1.txt2","heres some data2") 
    util.binfilewriter1("binfile1.bin","heres some binary data")

    pb = phonebook()
    pb.add_contact(p1)
    pb.add_contact(p2)
    pb.toCSV("phonebook1.csv")
    pb.fromCSV("phonebook1.csv")
    print(pb.contacts)
    print(pb.toJ3SON("phonebook.json"))
    pb.fromJ3son("phonebook.json") #need to work on json formating for this to work 
    pb.toyaml("phonebook.yaml")
    pb.fromyaml("phonebook.yaml")
    pb.topickle("phonebook.bin")
    print(pb.frompickle("phonebook.bin"))

    p1.toxml("person.xml")
    et = p1.fromxml("person.xml")
    print(et)



