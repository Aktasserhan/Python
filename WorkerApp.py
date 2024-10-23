class person():
    name=""
    surname=""
    id=""
    salary=""
    mission=""
    def setattr(self, name, surname,id,salary,mission):
        self.name=name
        self.surname=surname
        self.id=id
        self.salary=salary
        self.mission=mission
    def getattribute(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nSalary: {self.salary}\nMission: {self.mission}\n")


class manager(person):
    Authority="Limitless"
    def getattribute(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nSalary: {self.salary}\nMission: {self.mission}\nAuthority: {self.Authority}\n")

class officer(person):
    Authority="Paper work,and can sign"
    def getattribute(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nSalary: {self.salary}\nMission: {self.mission}\nAuthority: {self.Authority}\n")

class security(person):
    pass

class driver(person):
    pass

class worker(person):
    pass



p1 = driver()
p2 = driver()

p1.setattr("John", "Doe", "123", "5000", "Driver")
p2.setattr("Jane", "Smith", "456", "5500", "Driver")

p1.getattribute()
p2.getattribute()

# Manager Examples
p3 = manager()
p4 = manager()

p3.setattr("Erhan", "Aktaş", "034", "999999", "Manager")
p4.setattr("Bob", "Brown", "101", "8500", "Secont Manager")

p3.getattribute()
p4.getattribute()

# Officer Examples
p5 = officer()
p6 = officer()

p5.setattr("Charlie", "Williams", "202", "6000", "Officer")
p6.setattr("Diana", "Taylor", "303", "6200", "Officer")

p5.getattribute()
p6.getattribute()

# Security Examples
p7 = security()
p8 = security()

p7.setattr("Eve", "Davis", "404", "4000", "Security")
p8.setattr("Frank", "Wilson", "505", "4200", "Security")
p7.func()

p7.getattribute()
p8.getattribute()

# Worker Examples
p9 = worker()
p10 = worker()

p9.setattr("Grace", "Martinez", "606", "3500", "Worker")
p10.setattr("Henry", "Garcia", "707", "3700", "Worker")

p9.getattribute()
p10.getattribute()