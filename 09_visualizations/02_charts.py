"""
    차트, Seaborn
"""
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

from chart_config import setup, out
from merged_loader import load_merged

setup()
df = load_merged()

# 종몰별 일간 수익률(%)
df["ret"] = df.groupby("code")["close"].transform(lambda s: s.pct_change() *100)



# 히스토그램 => 분포 확인
fig, axes = plt.subplots(1, 2, figsize=(13,4))


axes[0].hist(df["ret"].dropna(), bins=60, color="steelblue")

axes[0].set_title("일간 수익률 분포")
axes[0].set_xlabel("수익률(%)")
axes[0].set_ylabel("빈도")

axes[1].hist(df["close"], bins=60, color="indianred")
axes[1].set_title("종가 분포")
axes[1].set_xlabel("수익률(%)")

fig.tight_layout()
fig.savefig(out("04_hist.png"), dpi=120)
plt.close(fig)

print(f"수익률: 평귱 {df['ret'].mean():.3f}%, 표준편차 {df['ret'].std():.3f}%")
print(f"종가 : 중앙값 {df['close'].median():,.0f}원, 최대값{df['close'].max():,.0f}원")



# seaborn으로 boxplot 그리기
fig, ax = plt.subplots(figsize= (13,5))

sns.boxplot(data=df, x="sector", y="ret", ax=ax)

ax.set_title("섹터별 일간수익률 분포")
ax.set_xlabel("섹터")
ax.set_ylabel("수익률(%)")

ax.tick_params(axis="x", rotation=30)

fig.savefig(out("05_box.png"),dpi=120)
plt.close(fig)

q1, q3 = df['ret'].quantile([0.25, 0.75])
iqr = q3 - q1
n_out = ((df['ret'] < q1 - 1.5 * iqr) | (df['ret'] > q3 + 1.5 * iqr)).sum()

print(f" Q1{q1:.3f} Q3 {q3:.3f}IQR {iqr:.3f}")
print(f" 범위 내 {q1 - 1.5 * iqr} ~ {q3 + 1.5 * iqr}")
print(f" 범위 밖 : {n_out:,}건")
# 섹터별로 이상치 선별해줘야 함

per_sector = 0

for name, g in df.groupby("sector"):
    a,b = g["ret"].quantile([0.25, 0.75])
    i = b - a

    per_sector += ((g['ret'] <a - 1.5 *  i) | (g['ret']> b + 1.5 * i)).sum()

print(f"섹터별 실제 이상치 합 : {per_sector:,}건")
print(n_out - per_sector)    


# 산점도
sample = df.dropna(subset=["ret"]).sample(5000, random_state=42)
# 무작위로 n행 뽑아줌

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

axes[0].scatter(sample['volume'], sample['ret'], s=6)
# scatter(x, y, s=점크기)
# s: 점 하나의 면적. 기본값 : 36

axes[0].set_title("산점도 (기본값)")
axes[0].set_xlabel("거래량")
axes[0].set_ylabel("수익률(%)")

axes[1].scatter(sample['volume'], sample['ret'], s=6, alpha=0.15)
axes[1].set_title("산점도(투명하게)")
axes[1].set_xlabel("거래량")

fig.tight_layout()
fig.savefig(out("06_scatter.png"), dpi=120)
plt.close(fig)


# 막대 그래프(barplot)
fig, ax = plt.subplots(figsize=(11,4))

sns.barplot(data=df, x="sector", y="ret", ax=ax)

ax.axhline(0, color="gray", lw=0.8)
ax.set_title("섹터별 평균 일간 수익률")
ax.set_xlabel("섹터")
ax.set_ylabel("평균 수익률(%)")
ax.tick_params(axis="x", rotation=30)

fig.savefig(out("07_bar.png"), dpi=120)
plt.close(fig)

by_sector = df.groupby("sector")["ret"].agg(["mean", "std", "count"])
print(by_sector.round(4))