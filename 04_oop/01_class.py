"""
클래스와 객체

- 기본 형태 -
class 클래스명:
    # 생성자
    def __init__(self):
        self.필드명 = 값

    # 메소드
    def 메소드명(self):
        pass
"""


# 기본 형태
class Account:

    # 생성자
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # 메소드
    def deposit(self, amount):
        self.balance += amount
        return self.balance


# 객체 생성
acc = Account("ㅂㅇㅇ", 10000)

print(f"owner : {acc.owner}")
print(f"balance : {acc.balance}")

print(f"deposit : {acc.deposit(7000)}")

print("=" * 60)


class Member:

    team_name = "리센느"
    count = 0

    # 생성자
    def __init__(self, name):
        self.name = name
        Member.count += 1


m1 = Member("원이")
m2 = Member("미나미")

print(f"m1.name : {m1.name}")
print(f"m2.name : {m2.name}")

print(f"m1.team_name : {m1.team_name}")
print(f"m2.team_name : {m2.team_name}")

print(f"count : {Member.count}")

m1.team_name = "RESCENE"

print(f"m1.team_name : {m1.team_name}")
print(f"Member.team_name : {Member.team_name}")