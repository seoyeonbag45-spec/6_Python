# name = input("이름 입력 :")
# gender = input("성별(M/F) 입력 :")
# age = input("나이 입력 :")
# height = input("키 입력 :")

# print(f"이름:{name}, 성별:{gender}, 나이:{age}, 키:{height}cm")


# ch = input("영문 소문자를 입력하세요:")

# print(f"소문자:{ch}")
# print(f"대문자:{ch.upper()}")


# x = int(input("첫 번째 정수를 입력하세요:"))
# y = int(input("두 번째 정수를 입력하세요:"))

# print(f" 합:{x+y}")
# print(f" 차:{x-y}")
# print(f" 곱:{x*y}")
# print(f" 몫:{x//y}")
# print(f" 나머지:{x%y}")

# x = int(input("첫 번째 정수를 입력하세요:"))
# y = int(input("두 번째 정수를 입력하세요:"))

# print(f"{x}의 제곱:{x*x}")
# print(f"{y}의 제곱근:{int (y**0.5)}")

# x = int(input("점수를 입력하세요(0-100):"))
# if x>=90 :
#     print("학점:A")
# elif x>=80 :
#     print("학점:B")
# elif x>=70 :
#     print("학점:C")
# elif x>=60 :
#     print("학점:D")
# else :
#     print("학점:F")            

# if x > 100 or x < 0 :
#     print("점수를 올바르게 입력하셈")

x = input("몸무게를 입력하세요(kg):")
y = input("키를 입력하세요(cm):")

print(f"BMI : type{(y/x*x)}")