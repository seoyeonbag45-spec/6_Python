"""
  컴프리헨션 
  - 간결하고 직관적 구조 생성 문법 (리스트, 딕셔너리 , 셋)
"""

#리스트
nums = []
for n in range(1, 6):
    nums.append(n)

print(f"nums : {nums}")    

# 리스트 컴프리헨션 => [표현식 for 변수 in 반복대상]
nums = [n for n in range(1, 6)]
print(f"nums (컴프리헨션) : {nums}")

nums = [n * n for n in range(1, 6)]
print(f"nums (컴프리헨션) : {nums}")
print()

# 조건에 해당하는 데이터만 포함할 때 => [표현식 for 변수 in 반복대상 if 조건]
nums = [1,2,3,4,5,6]
print(f"짝수만 --> {[n for n in nums if n % 2 == 0]}")
print(f"3의 배수만 --> {[n for n in nums if n % 3 == 0]}")

print("="*60)

# 딕셔너리 컴프리헨션 => {키_표현식:밸류_표현식 for 변수 in 반복대상 if 조건}
menus = ["ㄱㅂㅌ", "ㄷㄱㅂ", "ㅁㅁ", "ㅈㅇ"]

menus_dict = {m:len(m) for m in menus}
print(f"menus_dict : {menus_dict}")

munus_dict = {m:len(m) for m in menus if len(m) == 3}
print(f"menus_dict : {menus_dict}")

message = 'komorebi'

unique_chaar = {ch for ch in message}
print(f"'{message}'의 고유 문자 : {unique_chaar}")

unique_chaar = {ch for ch in message if ch != ',' and ch != ' '}
print(f"'{message}'의 고유 문자 : {unique_chaar} / ({len(unique_chaar)})")