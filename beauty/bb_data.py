import pandas as pd
import numpy as np

# ============================================
# 화장품 브랜드 BI 분석 실습 데이터 생성
# ============================================

np.random.seed(42)

n = 250

categories = [
    "스킨케어",
    "메이크업",
    "선케어",
    "클렌징",
    "바디케어"
]

channels = [
    "자사몰",
    "올리브영",
    "백화점",
    "온라인몰"
]

# 날짜 생성
dates = pd.date_range(
    start="2026-01-01",
    end="2026-08-31",
    periods=n
)

# 카테고리
category = np.random.choice(
    categories,
    size=n,
    p=[0.30, 0.25, 0.15, 0.15, 0.15]
)

# 판매 채널
channel = np.random.choice(
    channels,
    size=n,
    p=[0.30, 0.30, 0.15, 0.25]
)

# 가격
price = np.random.randint(
    10000,
    80000,
    size=n
)

# 판매량
sales_qty = np.random.randint(
    20,
    500,
    size=n
)

# 할인율
discount_rate = np.random.choice(
    [0, 5, 10, 15, 20, 30],
    size=n,
    p=[0.15, 0.15, 0.25, 0.20, 0.15, 0.10]
)

# 리뷰 평점
review_score = np.round(
    np.random.normal(
        loc=4.2,
        scale=0.45,
        size=n
    ),
    1
)

review_score = np.clip(
    review_score,
    1,
    5
)

# 반품률
return_rate = np.round(
    np.random.beta(
        2,
        25,
        size=n
    ) * 100,
    1
)

# DataFrame 생성
df = pd.DataFrame({
    "date": dates,
    "category": category,
    "channel": channel,
    "price": price,
    "sales_qty": sales_qty,
    "discount_rate": discount_rate,
    "review_score": review_score,
    "return_rate": return_rate
})


# ============================================
# 결측치 생성
# ============================================

# review_score 약 5%
missing_review = np.random.choice(
    df.index,
    size=int(n * 0.05),
    replace=False
)

df.loc[
    missing_review,
    "review_score"
] = np.nan


# return_rate 약 4%
missing_return = np.random.choice(
    df.index,
    size=int(n * 0.04),
    replace=False
)

df.loc[
    missing_return,
    "return_rate"
] = np.nan


# ============================================
# 의도적인 이상치 생성
# ============================================

# 비정상적으로 높은 판매량
df.loc[10, "sales_qty"] = 3500
df.loc[125, "sales_qty"] = 4200

# 비정상적으로 높은 반품률
df.loc[200, "return_rate"] = 48.0


# ============================================
# CSV 저장
# ============================================

df.to_csv(
    "business_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())

print("\n=== 데이터 크기 ===")
print(df.shape)

print("\n=== 결측치 ===")
print(df.isna().sum())

print("\nbusiness_data.csv 저장 완료!")