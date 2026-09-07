"""

"""
print("=" *60)  #"=" 문자열을 60번 반복 (곱하기)
print("기본 출력 확인")
print("=" *60)

print("hello, python!")
print('반가워, 파이썬!')

print(100)
print(3.14)
print(10+20)

print("임수진",20,"민트")

print("2026", "09", "07", sep="-")

print("=" * 60)
print("이스케이프 문자")
print("=" * 60)

print("이번 줄 다음에 출력하겠습니다.\n 한 줄 개행")
print("탭  간격을 주겠습니다. \t 한 탭 처리")
print("속마음 : \"재밌다\"")

print("=" * 60)
print("문자 형식 지정 (문자 포매팅)")
print("=" * 60)

name = "장재영 ♡"
age = 25
height = 168.4
position = "남자친구"

#java 의 printf 유사 
print("이름: %s, 직위 : %s,나이: %d, 키: %.1f" % (name, position, age, height))

#문자열 format() 메소드 사용
print("이름: {}), 나이: {}, 키:{}".format(name, age, height))

#f-sting : 문자열 표현 방법 (형식 지정)
print(f"이름: {name}, 나이: {age}, 키: {height}")
print(f"내년에는 {age +1}살이 됩니다.")

# - 정렬 기능 ({변수:옵션})
print(f"[{name:<10}]")
print(f"[{name:>10}]")
print(f"[{name:^10}]")

print("=" * 60)
print("입력 받아보기")
print("=" * 60)

age_str = input("나이 입력:")
print(f"입력값: {age}, 타입: {type(age_str)}")
#입력 값은 항상 문자열로 처리

#게산이 필요 경우 형변환
age = int(age_str)
print(f"입력값: {age}, 타입: {type(age)}")
print(f"내년 나이 : {age + 1}")

