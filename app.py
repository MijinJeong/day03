#inheritance
from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self._name = name #protected
        self._age = age
        print("Call Person()")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
    
    @abstractmethod#자식클래스에서 반드시 오버라이딩 해야함    
    def showinfo(self):
        pass

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)#부모의 기본 생성자를 따로 호출해주어야함 in python
        self.__major = major
        print("Call Student()")
    
    @property
    def major(self):
        return self.major
    
    @major.setter
    def major(self, value):
        self._major = value
    
    def show(self):
        print(f"{self._name, self._age, self.__major}")

    @staticmethod
    def staticshow():
        print("static 메서드 호출")
    
    @classmethod
    def clone(cls, obj):
        return cls(obj._name, obj._age, obj._major)
    #static_method = staticmethod(staticshow) 
    
    def showinfo(self):
        self.show()#delegator 대리자
    
class Employee(Person):
    def __init__(self):
        # super.__init__()
        print("Call Employeee()")
    def showinfo(self):
        return "Employee"

        
# p = Person("강감찬", 0)
s = Student("나학생", 15, "전자공학")
e = Employee()

# print(isinstance(p, Person))
# print(isinstance(p, object))

print(isinstance(s, Student))
print(isinstance(s, Person))
print(isinstance(s, object))

print(isinstance(e, Employee))
print(isinstance(e, Person))
print(isinstance(e, object))

s.show()
# print(s._name)
# Student.staticshow()
# s2 = Student.clone(s)
# print(id(s), type(s))
# print(id(s2), type(s2))

