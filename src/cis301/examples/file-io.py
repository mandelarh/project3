from cis301.objects.human import Human

class Person(Human):
    def __init__(self, name, Phone, Email):
        super().__init__(name)
        self.phone = Phone
        self.email = Email
    def __str__(self):
        return f"name:{self.name}\t phone:{self.phone}\t email: {self.email}\n"
    
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
        #returnf"{{"name:"{self.name} "phone:"{self.phone} email: {self.email}}}"
        pass

    
    @staticmethod
    def compare_by_email(p1,p2):
        if p1.email == p2.email:
            return 0
        elif p1.email < p2.email:
            return -1
        else:
            return 1
    
    def to_pickle(self, filename):
        with open(filename, 'w') as pickle_file:
            pickle.dump(self, filename)

    


    
    
if __name__ == '__main__':
    p1 = Person('mandela', '763-710-1431', 'mandela.haulcy@students.cau.edu')
    p2 = Person('wynton', '612-759-0233', 'ilovefood3901@gmail.com')

    if p1 == p2:
        print('its a match!')
    else:
        print('no match found')