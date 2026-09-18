"""
  연산자
"""

print("=" * 60)
print("산술 연산자")
print("=" * 60) 

print(f"7 + 3 = {7 + 3}")
print(f"7 - 3 = {7 - 3}")
print(f"7 * 3 = {7 * 3}")
print(f"7 / 3 = {7 / 3}")
print(f"7 // 3 = {7 // 3}")
print(f"7 % 3 = {7 % 3}")
print(f"7 ** 3 = {7 ** 3}") 
print()

print(f"실수 나눗셈 타입 : {type(7 / 3)}")
print(f"정수 나눗셈 타입 : {type(6 / 3)}")

print(f"-7 / 3 = {-7 / 3}")
print(f"-7 // 3 = {-7 // 3}")

print("=" * 60)
print("비교, 논리 연산자")
print("=" * 60) 

a,b = 2, 5
print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")  
print()

# 논리 연산자 : and, or, not

print(f"and --> {True and True}")
print(f"or --> {True or False}")
print(f"not --> {not True}")    

print(f"-5 <= a <=5 > 0 --> {-5 <= a <= 5 and a  <= 5}")

print(f"{-5 <= a <= 5 and a <= 5}")

print("=" * 60)
print("멤버쉽 연산자(in), 식별 연산자(is)")
print("=" * 60)

members = ["박이안", "김예원", "장재영"]
print(f"-> {members}")
print(f"'박이안' 포함 여부 -> {"박이안"in members}")
print(f"'김종혁' 포함 여부 -> {"김종혁"in members}")

print(f"'이광희' 포함 되지 않는지? -> {"이광희"in members}")

print(f"{'11' in 'hello'}")
print()

x = [1,2,3]
y = [1,2,3]
z= x
print(f"x = {x}, y = {y}, z = {z}")

print(f"배열 값 비교 : {x == y}")
print(f"객체 주소 비교 : {x is y}")
print(f"x is z : {x is z}")

#None 비교 시 is 사용 권장
data = None
print(f"data is none? {data is None}")
print(f"data is not none? {data is not None}")

print("=" * 60)
print("복합 대입 연산자")
print("=" * 60)

x = 10
print(f"x = {x}")

x += 5
print(f"x -= 5 : {x}")

x += 1

x -= 1
