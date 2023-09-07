import sys

def convert(string):
    if int(string) > 10:
        raise Exception('10이상이 입력되었습니다.')
    return int(string)

a, b = input('정수 두 개 입력: ').split()
try:
    a = int(a)
    b = int(b)
    c = a//b
    print(f"{a} // {b} = {c}")
except ZeroDivisionError:
    print("0으로 나누기가 실행되었습니다.", file=sys.stderr)
except TypeError | NameError:
    print("정의되지 않은 변수를 참조하거나 올바르지 않은 타입을 참조하였습니다.")
except Exception as e:
    print(e, file=sys.stderr) #e.__str__()
# else:
#     print("예외발생 안 함! else는 finally와 함께 사용하지 않음")
finally:    
    print('exit program')