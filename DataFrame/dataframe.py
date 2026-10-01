import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. csv 파일 불러오기
df = pd.read_csv("train.csv")
print('=' * 60)

# 2. 상위 5개 출력
print(df.head())
print('=' * 60)

# 3. 데이터 정보 확인
df.info()

# 결측치 개수 확인
print(df.isnull().sum())
print('=' * 60)

# 4. Age, Fare 평균 / 최소 / 최대
print("Age 평균 :", df["Age"].mean())
print("Age 최소 :", df["Age"].min())
print("Age 최대 :", df["Age"].max())

print("Fare 평균 :", df["Fare"].mean())
print("Fare 최소 :", df["Fare"].min())
print("Fare 최대 :", df["Fare"].max())

print('=' * 60)

# 5. 생존자 / 사망자 수
print(df["Survived"].value_counts())
print('=' * 60)

# 6. 객실 등급별 인원 수
print(df["Pclass"].value_counts())
print('=' * 60)

# 7. 50세 이상만 가져오기
age50 = df[df["Age"] >= 50]

print(age50)
print('=' * 60)

# 8. 나이대 만들기
bins = [0, 10, 20, 30, 40, 50, 60, 100]
labels = ["아동", "10대", "20대", "30대", "40대", "50대", "60대 이상"]
# pd.cut으로 나이대를 나눔
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels,
    right=False
)
# 새로운 분류값 "미확인" 추가
df["AgeGroup"] = df["AgeGroup"].cat.add_categories("미확인")

# 나이가 없는 사람은 "미확인"
df["AgeGroup"] = df["AgeGroup"].fillna("미확인")

print(df[["Age", "AgeGroup"]].head())
print('=' * 60)

# 9. 성별 + 객실 등급별 평균 생존율
result = df.groupby(["Sex", "Pclass"])["Survived"].mean()

print(result)
print('=' * 60)

# 10. 나이대별 평균 생존율
result = df.groupby("AgeGroup", observed=False)["Survived"].mean()

print(result)
print('=' * 60)

# 11. 결측치 개수와 비율
missing = pd.DataFrame()

missing["개수"] = df.isnull().sum()
missing["비율"] = df.isnull().mean() * 100

missing = missing.sort_values("비율", ascending=False)

print(missing)
print('=' * 60)

# 12. 성별을 숫자로 변경
df["Gender_Encoded"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

print(df[["Sex", "Gender_Encoded"]].head())
print('=' * 60)

# 13. 탑승지별 평균 요금
result = df.groupby("Embarked")["Fare"].mean()

print(result)
print('=' * 60)

# 14. 피벗 테이블
pivot = df.pivot_table(
    index="Pclass",
    columns="Sex",
    values="Fare",
    aggfunc="mean"
)

print(pivot)
print('=' * 60)

# 15. 가족 수 만들기
df["FamilySize"] = df["SibSp"] + df["Parch"]

print(df["FamilySize"].describe())
print('=' * 60)

# 16. 이름에서 호칭 추출
df["Title"] = df["Name"].str.extract(r", ([A-Za-z]+)\.")

print(df["Title"].value_counts().head())
print('=' * 60)

# 17. 호칭별 통계
result = df.groupby("Title").agg(
    승객수=("PassengerId", "count"),
    평균나이=("Age", "mean"),
    평균생존율=("Survived", "mean")
)

print(result)
print('=' * 60)

# 18. 생존자 / 사망자 나이 그래프
survived = df[df["Survived"] == 1]["Age"]
dead = df[df["Survived"] == 0]["Age"]

plt.hist(survived, bins=20, alpha=0.5, label="Survived")
plt.hist(dead, bins=20, alpha=0.5, label="Dead")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()

plt.savefig("age.png")
plt.close()


# 19. Title + Pclass별 나이 중앙값으로 결측치 채우기
median_age = df.groupby(
    ["Title", "Pclass"]
)["Age"].transform("median")

df["Age"] = df["Age"].fillna(median_age)

print(df["Age"].isnull().sum())
print('=' * 60)

# 20. 상관관계
cols = [
    "Survived",
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

corr = df[cols].corr()

print(corr)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()