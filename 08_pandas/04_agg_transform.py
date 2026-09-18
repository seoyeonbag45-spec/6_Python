import pandas as pd
from utils.loader import load_csv

#출력창 크기 설정
pd.set_option("display.width", 130)

#데이터 불러오기
df = load_csv()

# agg : 그룹 당 한 줄(행)

# 'code' 열을 기준으로 평균 조회
mean_by_code = df.groupby('code')['close'].mean()
print(f" 종목 코드별 평균 : {len(mean_by_code)}행")
print(mean_by_code.head().round())

#여러 개 한번에 집계
summary = df.groupby('code').agg(
            평균종가=("close", "mean"),
            최고가=("close", "max"),
            거래일수=("date", "count")
)
print(f" 통계 결과 : {len(summary)}행")
print(summary.head())

df['code_mean'] = df.groupby('code')['close'].transform('mean')
print(df.tail())