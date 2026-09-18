"""
실습용 사이트에서
종목 메뉴 페이지(SSR)의 섹터를 "IT서비스"로 검색한 결과 데이터 추출

요청 주소: ??
금일 6시까지 이메일 제출
"""
import requests
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks


# IT서비스(S08) 조건으로 SSR 페이지 요청
url = f"{BASE}/stocks?sector=S08&market=&q="

resp = requests.get(
    url,
    headers=HEADERS,
    timeout=TIMEOUT
)

# 요청 실패 시 예외 발생
resp.raise_for_status()


# HTML에서 종목 데이터 추출
items = parse_stocks(resp.text)


# 결과 출력
print(f"요청 주소: {url}")
print("=" * 60)

for data in items:
    print(f"{data['code']} : {data['name']} : {data['price']}")

print("=" * 60)
print(f"IT서비스 종목 수: {len(items)}")