PI = 3.14195

def hello():
    print('Hello')
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self): #toString과 유사
        return f"이름: {self.name}, 연령: {self.age}"

if __name__ == '__main__':
    print(PI)
    hello()
    p = Person('hong', 20)
    print(p)