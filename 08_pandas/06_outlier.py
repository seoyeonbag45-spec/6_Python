"""
 이상치 검색
"""
import pandas as pd
from utils.config import RAW_PATH,ENCODING, step_path

"""
raw-prices.csv 파일 읽어와서
'close' : int64/ float664 -> 콤마 포함된 것 모두 변환
'date' : datetime64   -> 형식 섞인 것 모두 변환
'code', 'date' 열 기준으로 중복 제거(첫 데이터 남김)
위 결과 df 변수에 저장
"""
df = pd.read_csv(RAW_PATH, encoding=ENCODING)
print(df.head())
df.info()

NUM_COLS = ['open', 'high', 'low', 'close', 'volume', 'change', 'changeRate']
for col in NUM_COLS:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(',','',regex=False),
        errors='coerce'
    )

# 날짜 변환 
df['date'] = pd.to_datetime(df['date'], format='mixed')

# 중복 제거
df = df.drop_duplicates(subset=['code', 'date'], keep='first').reset_index(drop=True)

# 결과
print(len(df))

step1_path = step_path('_step1.pkl')

print(" ===파일로 저장 ===")
df.to_pickle(step1_path)
print(" --- 저장 완료 ---")


print(" ===파일 읽어오기 ===")
df = pd.read_pickle(step1_path)
print(f" 파일 불러오기 완료 : {len(df)}행")
print(df.head())
print("=" * 60)

#이상치 확인
print(df['close'].describe().round(0))

# median 중앙값
# mean 평균

med = df.groupby('code')['close'].transform('median')
print(f"""
        [종목 중앙값과 비교]
        중앙값의 50배 초과 : {(df['close']>med * 50).sum()}건
        중앙값의 5% 미만 : {(df['close']>med * 0.05).sum()}건
""")

print('-'*60)

# quantile() : 값을 크기순으로 나열했을 때 특정 위치 값 구해주는 함수

q1, q3 =  df['close'].quantile([0.25, 0.75])
print(f"q1 : {q1}, q3: {q3}")

iqr = q3 - q1
lo = q1 - 1.5 * iqr
hi = q3 + 1.5 * iqr

out_mask = (df['close'] < lo) | (df['close'] > hi)

print(f" q1: {q1}, q3 : {q3}, iqr:{iqr}")
print(f"정상 데이터 범위 : {lo} ~ {hi}")
print(f"이상치 : {out_mask.sum()}건")

# IQR 로 이상치 탐지에 힌계 있음

tiny = df['close'] < med * 0.05
print(f"중앙값 5% 미만 : {tiny.sum()}건")
print(f" 이 중에 전체 IQR에도 속하는 건수 : {(tiny & out_mask).sum()}")

def is_outlier(data):
    """
        한 종목 종가데이터 받아 같은 길이 bool mask(T/F) 반환
        T 이상치
        F 정상데이터
    """
    data.quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return (data < lo) | (data > hi)

#종목별 이상치 (IQR)
result = df.groupby('code')['close'].transform(is_outlier)
print(f"종목별 : {result.sum()}")

result2 = (df["close"] > df["high"]) | (df['close'] < df['low'])
result3 = df['volume'] < 0
print(f"종가가 최저가, 최고가에서 벗어난 경우 : {result2.sum()}")
print(f"거래량이 음수인 경우 : {result3.sum()}")

#이상치 처리 => 결측치(NaN)로 처리
mask = result | result2

df.loc[mask, 'close'] = pd.NA

df['close'] = pd.to_numeric(df['close'], errors='coerce')

print()
print(f"이상치 (mask) : {mask.sum()}")
print(f"거래량 음수 (result3) : {result3.sum()}")
print(f"종가  결측수 : {df['close'].isna().sum()}")

print(" ===step2.pkl 저장 ===")
df.to_pickle(step_path('_step2.pkl'))