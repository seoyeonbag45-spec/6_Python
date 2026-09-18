import pandas as pd

from utils.loader import load_csv

pd.set_option('display.width', 130)

df = load_csv()

day = df[df['date'] == df['date'].max()].reset_index(drop=True)
print(day.head())
print('-'*60)

day['range'] = 0
print(day.head())
print('-'*60)

day['range'] = day['high'] - day['low']
day['range_pct'] = day['range'] / day['low'] * 100
print(day.head())
print('-'*60)

day['temp'] = 0
print(f"day shape : {day.shape}")

#열 이름 삭제
day = day.drop(columns=['temp'])
print(f"'temp'열 삭제 후 day shaoe : {day.shape}")
print('-'*60)

 #열 이름 변경
renamed = day.rename(columns={'close': '종가'})
print(f" 열 이름 변경 : \n{renamed.columns}")
print('-'*60)

# .str 접근자
# 문자열 메소드를 모든 행 일괄 적용
print(f"길이 len() -> {day['code'].str.len().unique().tolist()}")
print(f"슬라이싱 -> {day['code'].str[1:].head(3).tolist()}")
print(f"'G00'으로 시작하는 종목 코드 개수 -> {day['code'].str.startswith('G00').sum()}")
\
sample = pd.Series([" 가온전자", "해피바이오", "한빛중공업"])
print(f"공백 제거 --> {sample.str.strip().tolist()}")      

sample2 = pd.Series(["52000", "51500", "N/A", "1,240"])
print(f" sample2 : {sample2.tolist()}")

converted = pd.to_numeric(sample2, errors='coerce')
print(converted.tolist())
print(f"결측 ㅣ {converted.isna().sum()}")

c = pd.to_numeric(sample2.str.replace(',',''), errors='coerce')
print(c.tolist())
print(f"결츨 : {c.isna().sum()}")