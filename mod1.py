# ipynb파일은 확장자가 py가 아니므로 모듈로 사용할 수 없다!

PI = 3.14159


def add(num1, num2):
    return num1+num2

    pass # add

def sub(num1, num2):
    return num1-num2

    pass # sub



if __name__ == '__main__':
    
    # Test code
    print(add(100,200))
    print(sub(100,200))

    print(__name__)

    pass # if
pass # end class 