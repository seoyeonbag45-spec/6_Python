"""
    Matplotlib 으로 차트 생성
"""
import matplotlib

matplotlib.use("Agg")
#Agg (Anti-Grain Geometry)
# 화면(GUI 창)을 열지 않고, 메모리 내에서만 차트 표시(렌더링)
# 화면에 따로 출력 x, 파일로 저장할 떄 설정
# pyplot 임포트 하기 전 설정

import matplotlib.pyplot as plt

from chart_config import setup, out
from merged_loader import load_merged

setup()
df = load_merged()

one = df[df["code"] == "G0001"].sort_values("date")

fig, ax = plt.subplots(figsize=(12,4))

ax.plot(one['date'], one['close'])

ax.set_title("가온전자 주가 추이")
ax.set_xlabel("날짜")
ax.set_ylabel("종가(원)")
ax.grid(alpha=0.3)

fig.savefig(out('01_basic.png'))
#plt.show() -> 화면 띄워서 바로 차트 확인
# savefig() 와 show()같이 사용 시 savefig() 호출 후 show() 호출해야 함

fig, ax = plt.subplots(figsize=(10,3))
ax.plot(one["date"].iloc[:60], one['changeRate'].iloc[:60], marker=".")
# *marker= "." : 각 데이터 지점에 작은 점 표시

ax.axhline(0, color="gray", lw=0.8)
#axhline(y) : y 위치에 가로 기준선 표시 Lw - 선 굵기
ax.set_title("가온전자 일간 등락률")
ax.set_ylabel("등럭률(%)")

fig.savefig(out('02_minus.png'), dpi=120)

plt.close(fig)

"""
    * 필수 설정 항목
    ax.set_title("그래프 제목")
    ax.set_xlabel("x축 제목")
    ax.set_ylabel("y축 제목")
    ax.grid(alpha=0.3) 그리드 표시
    ax.legend() 범례 표시
"""
#그래프 여러 개 표시
codes = ["G0001", "G0002", "G0003", "G0004"]

fig, axes = plt.subplots(2,2, figsize=(13,6), sharex=True)
# 여러 개 차트 만드는 부분 

for ax, code in zip(axes.flat, codes):
    data = df[df["code"] == code].sort_values("date")

    ax.plot(data["date"], data["close"], lw=1)
    ax.set_title(f"{data['name'].iloc[0]} ({code})", fontsize=10)
    ax.grid(alpha=0.3)

fig.suptitle("종목별 주가 추이")
fig.tight_layout()

fig.savefig(out("03_subplots.png"), dpi=120)
plt.close(fig)

