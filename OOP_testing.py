
class Student:
    def __init__(self,name,group_number,age):
        self.name = name
        self.group_number = group_number
        self.age = age
    def getName(self):
        return self.name
    def getGroup_number(self):
        return self.group_number
    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setGroupNumber(self, group_number):
        self.group_number = group_number

    def setAge(self, age):
        self.age = age




hs1 = Student("Демьян", 33, 14)
print(f"Имя {hs1.name}")
print(f"Группа № {hs1.group_number}")
print(f"Возраст {hs1.age}")
hs1.setName("Максим")


hs2 = Student("Арина", 32, 13)
print(f"Имя {hs2.name}")
print(f"Группа № {hs2.group_number}")
print(f"Возраст {hs2.age}")
hs2.setAge(18)

