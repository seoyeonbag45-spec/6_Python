"""
    백터화 연산

    넘파이의 핵심 기능
    반복문 없이 연산 수행 가능 (빠름)
"""
import numpy as np
from load_utils import load_dates, load_codes, load_one_stock

dates = load_dates()        #거래일
codes = load_codes()
prices = load_one_stock(0)

a = np.array([10,20,30,40])
b = np.array([1,2,3,4])
print(f"a : {a}\b : {b}")
print(f"a * 2 = {a *2}")
print(f"a + b = {a + b}")
print(f"a > 25 = {a > 25}")

x = np.array([1,4,9,16])
print(f"x: {x}\nsqrt : {np.sqrt(x)}")

x = np.array([1.123423, 4.23423, 925234, 16.2356234])
print(f"x: {x}\nround : {np.round(x, 3)}")

x = np.array([-1, 4, -9, 16])
# abs(배열): 절댓값
print(f"x: {x}\nabs(x): {np.abs(x)}")

print(f"==={codes[0]} 750일 종가 ===")
print(f"전체 합: {prices.sum():,}")
print(f"전체 평균: {prices.mean():,.0f}")
print(f"전체 표준편차: {prices.std():,.0f}")
print(f"최고가: {prices.min():,.0f}")
print(f"최저가: {prices.max():,.0f}")

max_idx = prices.argmax()
min_idx = prices.argmin()

print(f"최고가: {prices.max():,.0f}")
print(f"최저가: {prices.min():,.0f}")


result = (prices[1:] - prices[:-1]) / prices[:-1]

print(f"일간 수익률 {len(result)}")
print(f"평균 : {result.mean() * 100:.4f}")
print(f"표준편차 : {result.std() * 100:.4f}")
print(f"최대 상승 : {result.max() * 100:.4f} ({dates[result.argmax() +1]})")
print(f"최대 하락 : {result.min() * 100:.4f} ({dates[result.argmin() +1]})")