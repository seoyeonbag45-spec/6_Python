import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import numpy as np
from matplotlib.ticker import FuncFormatter

df = pd.read_csv(
    "business_data.csv",
    encoding="utf-8-sig"
)

df["date"] = pd.to_datetime(df["date"])


# ==========================
# 한글 폰트 설정
# ==========================

if platform.system() == "Windows":
    plt.rcParams["font.family"] = "Malgun Gothic"

elif platform.system() == "Darwin":
    plt.rcParams["font.family"] = "AppleGothic"

plt.rcParams["axes.unicode_minus"] = False

# ==========================
#  원하는 색상 설정
# ==========================
cmap = sns.cubehelix_palette(
    start=2,
    rot=0,
    dark=0,
    light=.95,
    reverse=True,
    as_cmap=True
)
# ==========================================
# 과제 1
# 카테고리별 핵심 매출 분석
# ==========================================

# 1. 결측치 확인
print(df.isna().sum())

# 이상치
Q1 = df["sales_qty"].quantile(0.25)
Q3 = df["sales_qty"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["sales_qty"] < lower) |
    (df["sales_qty"] > upper)
]

print("=== 판매량 이상치 ===")
print(outliers)

# 2. 수치형 데이터 요약 통계 확인
print(df.describe())


# 3. 실제 매출 계산
df["revenue"] = (
    df["price"]
    * df["sales_qty"]
    * (1 - df["discount_rate"] / 100)
)


# 4. 카테고리별 매출 집계
category_sales = (
    df.groupby("category")["revenue"]
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)


# 5. Bar Chart
colors = [
    cmap(i)
    for i in np.linspace(0.2, 0.9, len(category_sales))
]

# 1억 원 단위로 변환
def billion_won(x, pos):
    return f"{x / 100_000_000:.0f}"

plt.figure(figsize=(10, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    hue=category_sales.index,
    palette=colors,
    legend=False
)

plt.title("카테고리별 매출")
plt.xlabel("카테고리")
plt.ylabel("매출 (억원)")

# Y축을 억원 단위로 변경
plt.gca().yaxis.set_major_formatter(
    FuncFormatter(billion_won)
)

# 가로선
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

plt.gca().set_axisbelow(True)

plt.tight_layout()
plt.show()


# ==========================================
# 과제 2
# 할인율과 판매량 관계 분석
# ==========================================


# 색상
palette = sns.cubehelix_palette(
    n_colors=df["category"].nunique(),
    start=2,
    rot=0,
    dark=0,
    light=.8,
    reverse=True
)

# 위쪽(이상치) / 아래쪽(정상 구간)
fig, (ax_top, ax_bottom) = plt.subplots(
    2, 1,
    sharex=True,
    figsize=(11, 7),
    gridspec_kw={
        "height_ratios": [1, 3],
        "hspace": 0.05
    }
)

# --------------------------
# 위쪽 : 이상치 구간
# --------------------------
sns.scatterplot(
    data=df,
    x="discount_rate",
    y="sales_qty",
    hue="category",
    palette=palette,
    s=55,
    alpha=0.7,
    ax=ax_top
)

ax_top.set_ylim(3400, 4400)

ax_top.set_yticks([
    3500,
    4000
])

ax_top.grid(
    True,
    linestyle="--",
    alpha=0.3
)

ax_top.set_ylabel("")


# --------------------------
# 아래쪽 : 정상 구간
# --------------------------
sns.scatterplot(
    data=df,
    x="discount_rate",
    y="sales_qty",
    hue="category",
    palette=palette,
    s=55,
    alpha=0.7,
    ax=ax_bottom
)

ax_bottom.set_ylim(0, 600)

ax_bottom.set_yticks([
    0, 100, 200, 300, 400, 500, 600
])

ax_bottom.set_xticks([
    0, 5, 10, 15, 20, 25, 30
])

ax_bottom.grid(
    True,
    linestyle="--",
    alpha=0.3
)

ax_bottom.set_xlabel("할인율 (%)")
ax_bottom.set_ylabel("판매량 (개)")


# --------------------------
# 중간 축 잘린 표시 //
# --------------------------
ax_top.spines["bottom"].set_visible(False)
ax_bottom.spines["top"].set_visible(False)

ax_top.tick_params(
    bottom=False,
    labelbottom=False
)

d = 0.008

kwargs = dict(
    transform=ax_top.transAxes,
    clip_on=False
)

ax_top.plot(
    (-d, +d),
    (-d, +d),
    color="black",
    **kwargs
)

ax_top.plot(
    (1-d, 1+d),
    (-d, +d),
    color="black",
    **kwargs
)

kwargs.update(
    transform=ax_bottom.transAxes
)

ax_bottom.plot(
    (-d, +d),
    (1-d, 1+d),
    color="black",
    **kwargs
)

ax_bottom.plot(
    (1-d, 1+d),
    (1-d, 1+d),
    color="black",
    **kwargs
)


# --------------------------
# 범례 하나만 표시
# --------------------------
ax_top.get_legend().remove()

ax_bottom.legend(
    title="카테고리",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

# 그리드를 점 뒤로
ax_top.set_axisbelow(True)
ax_bottom.set_axisbelow(True)

fig.suptitle(
    "할인율과 판매량의 관계",
    fontsize=14
)

plt.show()
# ==========================================
# 과제 3
# 판매 채널별 반품률 분포
# ==========================================

# 채널별 통계 확인
channel_return = (
    df.groupby("channel")["return_rate"]
      .agg(["mean", "median", "std"])
)

print(channel_return)


plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="channel",
    y="return_rate",
    hue="channel",
    palette=sns.cubehelix_palette(
        n_colors=df["channel"].nunique(),
        start=2,
        rot=0,
        dark=0,
        light=.8,
        reverse=True
    ),
    legend=False
)

plt.title("판매 채널별 반품률 분포")
plt.xlabel("판매 채널")
plt.ylabel("반품률 (%)")

plt.tight_layout()
plt.show()


# ==========================================
# 과제 4
# 카테고리 × 판매 채널 매출 Heatmap
# ==========================================

pivot = df.pivot_table(
    index="category",
    columns="channel",
    values="revenue",
    aggfunc="sum"
)

print(pivot)


plt.figure(figsize=(10, 6))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".0f",
    cmap=cmap
)

plt.title("카테고리 × 판매 채널 매출")
plt.xlabel("판매 채널")
plt.ylabel("제품 카테고리")

plt.tight_layout()
plt.show()