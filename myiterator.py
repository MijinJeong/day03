numbers = [1, 2, 3, 4, 5]

class NumberIterator:
    def __init__(self, list):
        self.__values = list
        self.__current = 0  #내부 반복자
        
    def __iter__(self):
        return self
    
    def __next__(self): #메서드가 호출되면 현재 반복자의 값이 반환됨
        if self.__current >= len(self.__values):    #반복자가 가리키는 값이 없으면 StopIteration을 전가함
            raise StopIteration #throw와 동일
        self.__current += 1
        return self.__values[self.__current -1]
    
    def get(self, index):
        if index >= len(self.__values) or index <0:
            raise Exception('잘못된 인덱스 참조입니다.')
        else:
            return self.__values[index]
        
    def seek(self):
        self.__current = 0
    
def next(iter):
    return iter.__next__()    
    
it = NumberIterator(numbers)
for i in range(0, 5):
    num = next(it)
    print(num)
# num = it.get(0)
# print(num)

it.seek()
for i in range(0, 5):
    num = next(it)
    print(num)
    
# it.seek()
# for i in it:
#     print(i)