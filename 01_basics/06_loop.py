"""
  반복문
"""

print("=" * 60)
print("for문 --> 항상 for-each")
print("=" * 60)

members = ["ㅂㅂㅂ", "ㅇㅇㅇ", "ㅈㅈㅈ"]

for m in members:
    print(f"{m}님, 환영합니다.")
print()

"""
for c in "Happy":
    print(c,)
"""

print("=" * 60)
print("range 내장 함수 사용")
print("=" * 60)

print(f"range(5) -> {list(range(5))}")
print(f"range(1,6) -> {list(range(1,6))}")

print(f"range(0,10,2)-> {list(range(0,10,2))}")
print(f"range(-5,0,1)-> {list(range(-5,0,1))}")
print(f"range(5,0,-1)-> {list(range(5,0,-1))}")

for i in range(5):
    print(f"i : {i}")
print()

for i in range(len(members)):
    print(f"[{i}] : {members[i]}")


print("=" * 60)
print("enumerate() - 번호와 값을 함께")
print("=" * 60)    

for i, m in enumerate(members):
    print(f"[{i}] : {m}")


for i, m in enumerate(members, start=1):
    print(f"[{i}] : {m}")

print("=" * 60)
print(" zip() - 여러 리스트를 동시에")
print("=" * 60)    

name = ["삼성", "sk", "애플"]
today = [200000, 300000, 400000]
yesterday = [220000, 300400, 400200]

for name, now, prev in zip(name, today, yesterday):
    diff = now - prev
    print(f"{name:<10} : {now:<8}원 ({diff})")


print("=" * 60)
print(" while ")
print("=" * 60)  

count = 0

while count < 5:
    print(f"count : {count}")
    count += 1
print()

n = 1
while True:
    if n > 3:
        break
    print(f"n : {n}")
    n += 1

print("장" * 60)

print("재" * 60)  
print("영" * 60)  

print("1~10 범위에서 홀수만 출력, 단 7일 넘으면 중단")
for n in range(1,11):
    if n % 2 == 0:
        continue
    if n > 7:
        break
    print(n, end=" ")
print()

print(f"{members}")

for m in members:
    if m == "ㅂㅂㅂ":
        print("찾았습니다")
        break
print()

for m in members:
    if m == "ㅇㅇㅈ":
        print("찾았습니다")
        break
else:        
    print("찾는 회원이 없습니다.")