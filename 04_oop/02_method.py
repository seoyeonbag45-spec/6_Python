"""
메소드 : 클래스 내의 함수

- 종류 - 
* 인스턴스 메소드
* 클래스 메소드 (@classmethod)
* 정적 메소드(@staticmethod)
"""

class Account:
    bank_name = "KH 은행"
    MIN_DEPOSIT = 1000

    def __init__(self, owner, balance = 0):
      self.owner = owner
      self.balance = balance

    #인스턴스 메소드 : 객체의 데이터를 다룸 
    def deposit(self, amount):
       self.balance += amount
       return self.balance  

    #클래스 메소드 : 클래스 자체를 다룸 
    @classmethod
    def from_dict(cls, data):
       """
        딕셔너리로부터 객체 생성하는 메소드
       """
       return cls(data["owner"], data.get("balance",0))

    #정적 메소드 : 객체, 클래스와 무관한 기능 담당 메소드(유틸리티). @staticmethod 지정
    @staticmethod
    def is_valid_amount(amount): 
       return amount >= Account.MIN_DEPOSIT

acc = Account("ㅂㅇㅇ", 10000)
print(f"deposit --> {acc.deposit(3000)}")

acc2 = Account.from_dict({"owner":"ㅂㅇㅇ", "balance":10000})
print(f"owner: {acc2.owner}, balance : {acc2.balance}")

print(f"amount: 6000 -> {Account.is_valid_amount(6000)}")
print(f"amount: 3000 -> {Account.is_valid_amount(3000)}")

""" 
    amount = 1500
    if Account.is_valid_amount(amount):
       print(f"deposit --> {acc2.deposit(amount)}")
    else:
       print(f"최소 금액을 만족하지 않습니다.")   
       """   

reponse = [
       {"owner": "ㅂㅇㅇ", "balance": 20000},
       {"owner": "ㅈㅇㅇ"},
       {"owner": "ㄱㅇㅇ", "balance": 40000}
    ]

accounts = [Account.from_dict(item) for item in reponse]

for a in accounts:
       print(f"{a.owner} {a.balance}원")


