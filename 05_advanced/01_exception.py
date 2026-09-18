"""
예외 처리

"""
def divide(text):
    try:
        num = int(text)
        result = f"60 / {num} = {60 / num}"
        # print(result)
    except ValueError:
        print(f"\"{text}'\" : 수로 변환할 수 없습니다.")
    except ZeroDivisionError:
        print(f"\"{text}\": 0으로는 나눌 수 없습니다.")
    except Exception as e:      # 별칭 부여
        print(f"{text} : {e}")
    else:       # 예외가 없을 때 실행되는 블록
        print(result)
    finally:
        pass    # 예외 발생 여부와 관계 없이 항상 실행되는 블록

for t in ["100", "-5", "abc", "0"]:
    divide(t)    

print("=" *60)

class NoBalnceError(Exception):
    """잔액 부족 예외"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super(). __init__(f"잔액 부족: 현재 {balance}, 요청: {amount}")

class InvalidAmountError(ValueError):
    """금액이 잘못된 경우 예외"""

class Account:
    """은행 계좌를 나타내는 클래스"""
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        """
          게좌에서 출금하는 메소드

          Args: 
            amount (int) : 출금할 잔액
        """    
        if amount <= 0:
            raise InterruptedError("출금액은 0보다 커야합니다.")

        if amount > self.balance:
            raise NoBalnceError(self.balance, amount)

        self.balance -= amount
        return amount

    def __str__(self):
        return f"[{self.owner}] 잔액 : {self.balance:,}원"

acc = Account("ㅇㅇㅇ", 30000)
print(acc)

for amount in [5000,50000,-1000]:

    try:
        acc.withdraw(amount)
        print(f"{amount:,}원 출금 완료")
        print(acc)

    except NoBalnceError as e:
        print(f"출금 실패 : e")

    except InvalidAmountError as e:
        print(f"출금 실패 : {e}")
    else:
        print(f"출금 성공 :")    


   #todo : 저기 예외처리하기 for