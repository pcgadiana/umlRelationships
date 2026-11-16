from abc import abstractmethod


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = person("Prince", 69420)
print("Name : " + person1.name) 
print("Age : " + str(person1.age))

#2
class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    

    def get_age(self):
        return self.__age

person1 = person("Prince", 69420)
print("Name : " + person1.name)
print("Age : " + str(person1.get_age()) + " (note this age is privately accessed)")

#3
class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    

    def get_age(self):
        return self.__age

class Student(person):
    def study(self):
        print(f"{self.name} is studying.")
student1 = Student("Prince", 69420)
print("Name : " + student1.name)
print("Age : " + str(student1.get_age()) + " (note this age is privately accessed)")
student1.study()

#4

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    

    def get_age(self):
        return self.__age

class Student(person):
    def study(self):
        print(f"{self.name} is studying.")
class Teacher(person):
    def teach(self):
        print(f"{self.name} is teaching.")

student1 = Student("Prince", 69420)
print("Name : " + student1.name)
print("Age : " + str(student1.get_age()) + " (note this age is privately accessed)")
student1.study()
Teacher1 = Teacher("Rocco", 420)
print("Name : " + Teacher1.name)
print("Age : " + str(Teacher1.get_age()) + " (note this age is privately accessed)")
Teacher1.teach()   

#5
class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    

    def get_age(self):
        return self.__age
    
    def describe(self):
        pass
class student(person):
    def describe(self):
        print("name : " + self.name)
        print("age : " + str(self.get_age()) + " (note this age is privately accessed)")
        print(self.name + " is studying.")
        print(self.name + " is a student.")
class teacher(person):
    def describe(self):
        print("name : " + self.name)
        print("age : " + str(self.get_age()) + " (note this age is privately accessed)")
        print(self.name + " is teaching.")
        print(self.name + " is a teacher.")
person1 = student("Prince", 69420)
person1.describe()
teacher1 = teacher("Rocco", 420)
teacher1.describe()

#6
class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    

    def get_age(self):
        return self.__age
    
    @abstractmethod
    def describe(self):
        pass

class student(person):
    def describe(self):
        print("name : " + self.name)
        print("age : " + str(self.get_age()) + " (note this age is privately accessed)")
        print(self.name + " is studying.")
        print(self.name + " is a student.")
class teacher(person):
    def describe(self):
        print("name : " + self.name)
        print("age : " + str(self.get_age()) + " (note this age is privately accessed)")
        print(self.name + " is teaching.")
        print(self.name + " is a teacher.")
person1 = student("Prince", 69420)
person1.describe()
teacher1 = teacher("Rocco", 420)
teacher1.describe()