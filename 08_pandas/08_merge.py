from utils.loader import load_prices,load_companies

prices = load_prices()

companies = load_companies()
raw_comp = load_companies(True)

print(f'prices : {len(prices)}')
#print(companies.head())
#print(companies.columns)
print(f"섹터 개수 : {companies['sectorCode'].nunique()}")
print(f"종목 개수 : {len(companies)}")


"""
    시세(prices) 90,000행에 섹터이름을 매번 저장하면
            같은 문자열이 수천번 반복될 것임!
        => 분리해서 저장하고 식별코드로 연결해줌! (정규화)

    저장할 때는 나누고, 분석할 때는 합쳐서 진행!
    = 나누어져 있는 데이터를 다시 붙여주는 것 : merge
"""


#print(prices.head(1))
#print(companies.head(1))

m = prices.merge(companies, on='code', how='left')
print(f" prices + companies :: how=inner")
print(f" - prices : {prices.shape}")
print(f" - merged : {m.shape}")

p2 = prices.head(3).copy()
p2['name'] = '시세데이터_이름'

m2 = p2.merge(companies[['code', 'name']], on='code')
print(m2)


m3 = p2.merge(companies[['code', 'name']], on='code', suffixes=('_price', '_company'))
print(m3)

#  1. 문자열의 공백이 있는 경우 동일한 값이 아님
# 앞뒤 공백 있는 
blk_edge = (raw_comp['name'] != raw_comp['name'].str.strip()).sum()

# 중간에 공백 있는
blk_mid = (raw_comp['name'].str.contains(r"\S\s+\S", regex=True)).sum()

print(f" === 공백 체크 === ")
print(f" 앞 뒤 공백 : {blk_edge}건")
print(f" 중간 공백 : {blk_mid}건")

# 2. 대소문자
print("===  대소문자 체크 ===")


# 3. 전각문자
def has_fullwidth(s):
    """
        전각 문자가 하나라도 있으면 True 반환

        ord(문자) : 해당 문자의 유니코드 번호 반환

    """
    return any( (0xFF01 <= ord(ch) <= 0xFF5F) or (ord(ch) == 0x3000) for ch in str(s))

# map(함수) : 대상(시리즈) 하나하나에 함수를 적용한 반환값으로 새롭게 동일한 타입(시리즈)으로 반환
fw = raw_comp[raw_comp['name'].map(has_fullwidth)]
print(f" ===전각 문자 체크 ===\n {len(fw)}건")
print(fw)

# 4. 타입 불일치
c1 = companies.copy()
c1['code_num'] = c1['code'].str.replace('G','').astype('int64')

p1 = prices.head(100).copy()
p1['code_num'] = p1['code'].str.replace('G','')

print(f"c1 : {c1['code_num'][0]} {c1['code_num'].dtype}")
print(f"p1 : {p1['code_num'][0]} {p1['code_num'].dtype}")

"""
r1 = p1.merge(c1, on='code_num')
print(r1)
기준 열의 타입이 다르면 merge 시 오류 발생
"""
print("=" *60)

# outer merge 를 활용해 매칭 되지 않은 데이터 확인 가능

# 특정 종목 제외
part = companies[ companies["code"] != "G0001"]

chk = prices.merge(part, on='code', how='outer', indicator=True)

print(f"{chk['_merge'].value_counts()}")

#  both : 양쪽
#  left_only : 왼쪽(prices)에서 옴
#  right_only : 오른쪽(part)에서 옴

# how=inner 로 머지했을 때, 행이 줄었다면 확인이 어려우므로
#    how=outer, indicator=True 설정하여 어떤 데이터가 빠졌는 지 확인할 수 있음