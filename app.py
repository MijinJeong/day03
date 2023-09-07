class Person:
    def __init__(self, name, age):
        self._name = name #protected
        self._age = age
        print("Call Person()")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)#부모의 기본 생성자를 따로 호출해주어야함 in python
        self.__major = major
        print("Call Student()")
        
    def show(self):
        print(f"{self.__name, self.__age, self.__major}")
        
class Employee:
    def __init__(self):
        print("Call Employeee()")
        
p = Person("")
s = Student()
e = Employee()

print(isinstance(p, Person))
print(isinstance(p, object))

print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(s, object))

print(isinstance(e, Employee))
print(isinstance(e, Person))
print(isinstance(e, object))

s.show()
print(s._name)
