"""
   함수

   - 정의 시 사용하는 키워드 : def
"""
print("=" * 60)

# 함수 정의
def hello(name):
    return f"{name}님 안녕하세요."

# 함수 사용 
hello("ㅂㅇㅇ")
result= hello("ㅂㅇㅇ")
print(result)

def hello_print(name):
    print(f"{name}님 반갑습니다.")
    #return 없음 (생략)

hello_print("ㄱㅇㅇ")
print(hello_print("ㅂㄱㅇ")) #반환값이 없는 건 None 반환
result = hello_print("ㅈㅇㅇ")
print(f"result : {result}")
print()

# 여러 값을 반환
def calc(a, b):
    return a + b, a - b, a * b

result = calc(5, 7)
print(f"결과 : {result}")

# 언패킹 => 여러 변수로 나누어 저장
add, sub, mul = calc(5,7)
print(f"결과 : {add} {sub} {mul}")

print("=" * 60)
print(" docstring (함수 설명)")
print("=" * 60)

def calc_tax(price, rate = 0.1):
    """
    부가세를 포함한 최종 금액 반환 함수

    """
    return int(price * (1 + rate)) 

print(f"10000원 ---> {calc_tax(10000):,}")
help(calc_tax)

print(test())

def test():
    return "테스트 함수입니다"