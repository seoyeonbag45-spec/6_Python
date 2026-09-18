"""
   집합 set
"""

#중복 불가, 순서x, 수정0

nums = {1,2,3,3,3,4,2}
print(f"nums : {nums}")

#비어 있는 상태 표현
empty1 = {}  
empty2 = set()

print(f"empty1 : {type(empty1)}")
print(f"empty2 : {type(empty2)}")
print()

nums = [1,2,3,3,3,4,2]
print(f"원본 데이터 : {nums}")
print(f"중복 제거 : {set(nums)}")
print(f"중복 제거 : {list(set(nums))}")
print()

#집합 연산
a = {1,2,3,4}
b = {3,4,5,6}

print(f"합집합 | : {a|b}")
print(f"교집합 & : {a & b}")

#데이터 변경
data = {1,2}
print(f"data : {data}")

data.update([4,5])
print(f"data : {data}")

data.update([4,5,6,7])
print(f"data : {data}")

data.discard(1)
print(f"data : {data}")

data.discard(99)
print(f"data : {data}")
