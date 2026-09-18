"""
 조건문
"""

print("=" * 60)
print("if / elif / else")
print("=" * 60)

value = 10

if value > 5:
    print("조건문 내부입니다.")
    print("조건문 내에서 실행하고자 하면 들여쓰기 필수")

print("조건문 외부입니다.")
print()

score = int(input("점수 입력 : "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "c"
else: 
    grade = "F"

print(f"{score}점 => {grade}")   
print() 

print("=" * 60)
print("삼항 연산")
print("=" * 60)

age = int(input("나이 입력:"))
"""
if age >= 20:
    result = "성인"
else:
    result = "미성년자"        
"""
result = "성인" if age >= 20 else "미성년자"
print(f"{age}세 -> {result}")

"""

print("=" * 60)
print("match-case (java의 switch)")
print("=" * 60)

match status:
    case 200:
        result = "정상"
    case 404:
        result = "페이지 찾을 수 없음"
    case 500:
        result = "서버 오류"
    case _:
        result = "알 수 없음"

print(f"{status}-> {result}")
"""

print("=" * 60)
print(" pass ")
print("=" * 60)

score = 90

if score > 90:
    pass # 미구현 부분 임시 처리
else:
    print("---- else 영역 ----")
    










