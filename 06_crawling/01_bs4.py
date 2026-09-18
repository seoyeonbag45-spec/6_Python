"""
 BeautifulSoup
 :HTML 및 XML 문서에서 원하는 데이터를 쉽게 추출할 수 있도록 해주는 스크래핑 라이브러리

 1.request 로 요청 후 문자열 (html, xml)을 응답 받음
 2.bs4의 find, select 를 활용해서 특정 텍스트 추출
"""
import requests
#=> 해당 모듈 설치 필요 pip install requests
from bs4 import BeautifulSoup

from config import BASE, TIMEOUT, HEADERS

resp = requests.get(f"{BASE}/stocks", headers=HEADERS, timeout=TIMEOUT)
resp.raise_for_status()

html = resp.text
print(f"{BASE}/stocks  [{resp.status_code}] {len(html):,}자")

print('-' *60)

soup = BeautifulSoup(html, 'lxml')

print(f"title --> {soup.title.text if soup.title else '없음'}")

# 기존에 자바 스크립트 통해 DOM 조작처럼
# bs이 같은 역할 함

# select : CSS 선택자 사용해 해당 요소 반환. 없는 경우 []
# select_one : CSS 선택자 사용해 해당 요소 1개 반환. 없는 경우 None

row_select = soup.select("tr.stock-row")
print(f"tr.stock-row 개수 : {len(row_select)}")

first = soup.select_one("tr.stock-row")
price_tag = first.select_one("td.col-price")
print(f"td.col-price text  : {price_tag.text}")
print(f"td.col-price text  : {price_tag.text!r}")

#f-string 에서 !r사용 시 repr() 이 호출되어 
# 숨겨진 공백(\ㅜ, \t 등)까지 그대로 출력해줌

print(f"td.col-price text  : {price_tag.get_text()!r}")
print(f"td.col-price text  : {price_tag.get_text(strip=True)!r}")

# 속성값 추출 --> get()
name_link = first.select_one("td.col-name a")

print(f"name_link['href] : {name_link['href']}")
print(f"name_link.get('href) : {name_link.get('href')}")
print(f"name_link.get('href) : {name_link.get('href','없음')}")

# 첫 번째 행 전체 데이터 추출
for sel in ["td.col-code", "td.col-name a", "td.col-sector",
            "td.col-price", "td.col-change", "td.col-volume", "td.col-market span"]:
    tag = first.select_one(sel)
    value = tag.get_text(strip=True) if tag else "없음"
    print(f"{sel:<20} {value}")