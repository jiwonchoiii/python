#변수의 종류와 유효범위(scope)에 대해 알아보자

a = 100  # 전역변수: 이 소스코드가 끝날 때 까지만.

# 함수의 매개변수와 함수블록 내에서 선언된 변수는 그 윻범위가 함수블록 내에서만 윻하다. 매개변수와 지역변수는 함수가 호출될 때 생성되고, 함수호출이 끝나면 자동으로 파괴된다. 
def func(parg): # 매개변수도 지역변수로 '간주'한다.
    b = 1000
    print(b)

    pass # func


func(7777)

print(a)
print(b)
print(c)
