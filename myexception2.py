from sys import stderr

class MyError(Exception):#사용자 정의 예외
    def __init__(self, msg='미원'):
        pass
        # super().__init__(msg)
        

def convert(string):
    try:#하나의 에러로 통일해서 던지는 방법
        if int(string) >= 10:
            raise MyError('10이상이 입력되었습니다.')
        return int(string)
    except ValueError as e:
        raise MyError("숫자로 변환할 수 없는 예외가 발생하였습니다.")
    except MyError as e:
        raise e

a = input('정수 입력: ')

try:
    num = convert(a)
    print(f"입력 받은 값: {num}")
except MyError as e:
    print(e)