from functools import reduce

"""
 람다식과 고차함수
"""
print("=" * 60)
print("lambda - 익명함수")
print("=" * 60)

def double1(x):
    return x * 2

print(f"일반 함수 : {double1(77)}")

double2 = lambda x: x * 2
print(f"람다 함수 : {double2(7)}")

print("=" * 60)
print("고차 함수")
print("=" * 60)

# map() : 전달한 함수 적용해 새로운 리스트 반환
numbers = [n for n in range(1,7)]
print(f"numbers: {numbers}")

result = list(map(lambda x: x * 2, numbers))
print(f"map 활용 : {result}")

#filter() : 조건을 만족하는 요소만 가지고 새로운 이터레이터 반환
result = list(filter(lambda x: x% 2 == 0, numbers))
print(f"filter 적용 : {result}")

# sorted() : 데이터 정렬
numbers = [15,26,7,3,41,17]
print(f"numbers : {numbers}")
print(f"오름차순 정렬: {sorted(numbers)}")
print(f"내림차순 정렬: {sorted(numbers, reverse=True)}")
print()

products = [
    {"name":"로지텍 키보드", "price":20000},
    {"name":"손목 쿠션", "price":50000},
    {"name":"로지텍 마우스", "price":100000},
]
print(f"products: {products}")

by_price = sorted(products, reverse=True, key=lambda p:p['price'])
for p in by_price:
    print(f"{p['name']} : {p['price']}")
print()

# 이름(name) 기준으로 오름차순 정렬
for p in sorted(products, key=lambda x: x['name']):
    print(f"{p['name']} : {p['price']}")
print()

#reduce : 순화하면서 누적 게산 수행 함수
numbers = [10,20,30]
print(f"{reduce(lambda total, curr: total + curr, numbers, 0)}")

datas = ["apple", "cat", "blueberry", "moon"]

longest = reduce(lambda result, curr: result if len(result) >= len(curr) else curr, datas)
print(f"결과 --> {longest}")

numbers = [3,5,2,1,9,7]
print(f"길이 : {len(numbers)}")
print(f"총합 : {sum(numbers)}")
print(f"최댓값 : {max(numbers)}")
print(f"최솟값 : {min(numbers)}")

print(f"any: {any(n> 5 for n in numbers)} ")
print(f"all: {all(n> 5 for n in numbers)} ")