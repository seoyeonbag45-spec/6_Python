"""
    Pandas 판다스

    Numpy(넘파이) 기반의 데이터 구조 제공
    SQL 처럼 다양한 조작, 분석 기능 제공 라이브러리
"""
import pandas as pd
from utils.config import RAW_PATH,ENCODING

"""
    Series : 라벨링된 1차원 배열 구조
"""
datas = [10,20,30,40]

#시리즈 생성
s = pd.Series(datas)
print(s)

print(f"index : {s.index} / {s.index.to_list()}") #인덱스 정보
print(f"values : {s.values} ({type(s.values).__name__})")
print('-' *60)

s = pd.Series(datas, name="sample")
print(s)
print(f"name : {s.name}")
print(f"index : {s.index}")
print(f"values : {s.values}")
print('-' *60)

s = pd.Series(datas, index=['a', 'b', 'c', 'd'])
print(s)
print(f"index : {s.index}")
print('-' *60)

s1 = pd.Series([10,20,30], index=['x','y','z'])
s2 = pd.Series([1,2,3], index= ['x','y','z'])

print("=== s1 ===")
print(s1)
print("=== s2 ===")
print(s2)
print()

print(f"s1 + s2 = \n{s1 + s2}")
# 연산 수행 될 때 순서아닌 인덱스 기준으로 연산 수행됨
# => 인덱스 같은 것 끼리 연산됨

s3 = pd.Series([1,2], index=['x', 'w'])
print("=== s3 ===")
print(s3)
print()

print(f"s1 + s3 = \n{s1 + s3}")
#연산이 수행될 때, 동일한 인덱스가 없을 경우 NaN이 됨

print("=" *60)

"""
    DataFrame : 2차원 테이블 구조
    - Series 를 여러 개 묶어서 만든 2차원 구조
    - 행(인덱스)과 열(컬럼)로 구성
"""
data = {
    "이름" : ["하루견과", "뼈건강비타민", "페레로로쉐"],
    "가격" : [2000, 4000, 3500],
    "재고" : [10, 5, 20]
}
#DataFrame 생성
df = pd.DataFrame(data)
print(df)

print(f"dtypes : \n{df.dtypes}") #각 열 데이터 타입
print(f"shape : {df.shape}") #행, 열 개수
print(f"index : {df.index}") #행 인덱스
print(f"columns : {df.columns}") #열 이름

print('-' * 60)
"""
print("RAW_PATH =", RAW_PATH)
print("존재 여부 =", RAW_PATH.exists())

df = pd.read_csv(RAW_PATH, encoding=ENCODING)
"""
#파일로부터 읽어와서 생성

# CSV (Comma Seperated Values) : 쉼표로 구분되어 있는 데이터

# pd.read_csv(파일명) => DataFrame

df = pd.read_csv(RAW_PATH, encoding=ENCODING)

print(df.head())
print(f"close dtype : {df['close'].dtype}")
print(f"date dtype : {df['date'].dtype}")

print('-' * 60)

df = pd.read_csv(RAW_PATH,
                 encoding=ENCODING,
                 parse_dates=["date"],
                 na_values=["N/A", "-"],
                 thousands=","
                 )

print(df.head())
print(f"close dtype : {df['close'].dtype}")
print(f"date dtype : {df['date'].dtype}")

print(f"date unique : {df['date'].unique()}") #중복 제거 결과


df['date'] =pd.to_datetime(df['date'], format='mixed')
print(f"to_datetime -> {df['date'].dtype}")

print(df.head(3))

# df.shape : 불러온 데이터 행, 열 개수
print(df.shape)

 #df.info() : 불러온 데이터 컬럼별 데이터 개수, 타입 등 확인
df.info()

#df.dtypes : 컬럼별 데이터 타입
print(df.dtypes)