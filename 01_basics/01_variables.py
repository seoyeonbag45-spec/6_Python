"""
변수와 자료형
"""

name = "박이안"
age = 25
height = 166.4
is_tired = True
temp = None

print(name, age, height, is_tired, temp)

print("=" * 60)
print("기본 자료형 5가지")
print("=" * 60)

#변수에 저장된 데이터 타입 확인
print(f"{name} : {type(name)}")
print(f"{age}: {type(age)}")
print(f"{height}: {type(height)}")
print(f"{is_tired}: {type(is_tired)}")
print(f"{temp}: {type(temp)}")

print("=" * 60)

value = 27
print(f"{value} : {type(value)}")
value = "스물일곱"
print(f"{value}: {type(value)}")

#이전 저장 타입과 이후 저장 타입 달라도 저장 가은
# 혼란 방지 위해 하나 변수에 하나 타입 사용 권장

print("=" * 60)

# 다중 할당
x, y, z = 10, 20, 30
print(f"x, y, z -> {x}, {y}, {z}")

a = b = c = 0
print(f"a = b = c -> {a}, {b}, {c}")

#값 교환
x, y = y, x
print(f"x, y -> {x}, {y}")

print("=" * 60)

# 타입 힌트 
menu: str = "ㅈㅇ"
print(f"menu: {menu} ({type(menu)})")

price: int = "12000원"
print(f"price : {price} ({type(price)})")

print("=" * 60)
MAX_PERSON = 60
print(f"최대 인원 : {MAX_PERSON}")
