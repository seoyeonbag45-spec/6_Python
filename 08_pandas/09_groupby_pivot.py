import pandas as pd
from utils.loader import load_merged

df = load_merged()
print(f"통합 데이터 : {len(df)}행 / {df['code'].nunique()}종목 / {df['sector'].nunique()}섹터")
"""
agg : 요약표 만들 떄 그룹 별로 결과 도출
transform : 원본에 열 추가해 값 비교할 때, 그룹별고 계산 결과 원본과 동일 도출
filter : 그룹 별로 검사해 조건 안 맞으면 제외

"""
two =  df[df["code"].isin(["G0001", "G0002"]) ].reset_index(drop=True)
print( two[["code", "date", "close"]].head(6) )

#diff() : 바로 위 행과의 차이를 반환

wrong = two["close"].diff()
right = two.groupby("code")["close"].diff()

#shift() : 열 통쨰로 한 칸 아래로 밀어줌

boundary = two.index[ two['code'] != two['code'].shift() ][1]
#print(boundary[1])
print(f"종목이 바뀌는 지점: {boundary}")

for i in range(boundary - 2, boundary + 2):
    w = f"{wrong[i] if pd.notna(wrong[i]) else 'NaN'}"
    r = f"{right[i]}" if pd.notna(right[i]) else "NaN"

    print(f" {i:<8} {two.loc[i, 'code']:<9} {two.loc[i, 'close']:<12}{w:>20} {r:>20}")

print("=" *60)

count_num = df.groupby("sector")["code"].count()
nunique_num = df.groupby("sector")["code"].nunique()

print(f"count : {count_num}")
print(f"nunique : {nunique_num}")

# agg : 요약표
summary = df.groupby("sector").agg(
                종목수=("code", "nunique"),
                거래일수=("date", "count"),
                평균종가=("close", "mean"),
                최대거래량=("volume", "max")
            )

print(summary.round(0))
print("=" *60)

#filter : 그룹 단위로 걸러냄. 조건 만족하는 그룹 전체 남겨줌
# 거래일이 700일 미만인 종목 제외
filtered = df.groupby("code").filter(lambda g: len(g) >= 700)
print(f" {len(df)}행 {df['code'].nunique()}종목 ")
print(f" -> {len(filtered)}행 {filtered['code'].nunique()}종목 ")

print("=" *60)

multi = df.groupby(["sector", "market"])["close"].mean()
print(f"인덱스 타임 : {type(multi.index).__name__}")
print(multi.head(6).round(0))

print("인덱스의 첫번쨰 레벨로 조회 (sector)")
print(multi.loc['금융'].round(0))

print("인덱스의 모든 레벨 지정 -> 튜플로 전달")
print(multi.loc[('금융', 'GX-GROWTH')])
print()

#unstack() : 인덱스를 열로 펼침
print(multi.unstack().head(4).round(0))
# => 인덱스 안쪽 레벨 값 열로 올림
print()

#reset_index() : 인덱스 열로 되돌림
print(multi.reset_index().head(3).round(0))
"""
  sector     market    close
0  IT서비스  GX-GROWTH  42250.0
1  IT서비스    GX-MAIN  70300.0
2     건설  GX-GROWTH  13168.0

"""

#groupby : 처음부터 그룹화 기준이 열로 나옴
flat = df.groupby(['sector', 'market'], as_index=False)['close'].mean()
print(flat.columns.tolist())


"""
pivot_table : 한 열은 행으로, 다른 열을 열로 펼쳐서 집계

"""
d = df.copy()

#분기 정보 추가
d['quarter'] = d['date'].dt.to_period("Q").astype(str)
# tp_period() : 날짜 기간으로 변경

pv = d.pivot_table(
    index="sector", 
    columns="quarter", 
    values="close", 
    aggfunc="mean"
)
print(pv.iloc[:5, :4].round(0))
print("=" * 60)

# 넓은 형식 , 긴 형식
wide = pv.iloc[:3, :3]
print("== 넓은 형식 ==")
print(wide.round())   # 사람이 보기 편함

# melt : 넓은 형식을 긴 형식으로 녹여서 표현
#    df.melt(id_vars=유지할_열, var_name=열이름을_담을_열, value_name=값을_담을_열)
#    => 열마다 흩어져 있는 값을 하나의 열에 모으기 위함
long = wide.reset_index().melt(id_vars="sector", var_name="quarter", value_name="close")
print("== 긴 형식 ==")
print(long.head(6).round())
# DB 저장, 시각화할 때 활용

# 피봇 -> 사람이 보는 보고서, 엑셀, 데이터 확인 시 활용

back = long.pivot(index="sector", columns="quarter", values="close")
print(back.round())