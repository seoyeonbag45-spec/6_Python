import requests
from config import BASE, TIMEOUT, HEADERS
from parsers import parse_stocks

#ssr : server side rendering 서버에서 완성된 화면 응답
#csr : client side rendering 빈 html을 서버로부터 응답받고, 자바스크립트 통해 데이터 화면에 표시

ssr = requests.get(f"{BASE}/stocks", headers=HEADERS, timeout=TIMEOUT)
csr = requests.get(f"{BASE}/csr/stocks", headers=HEADERS, timeout=TIMEOUT)

print(f"{'경로':<20}{'상태':8}{'본문 길이':>12}")
print(f"{'/stocks (SSR)':<20}{ssr.status_code:<8}{len(ssr.text):>12}")
print(f"{'/csr/stocks (CSR)':<20}{csr.status_code:<8}{len(csr.text):>12}")

for line in csr.text.strip().strip().split("\n"):
    print(f"{line}")

KEYWORD = '가온전자'
print(f"ssr --> {KEYWORD in ssr.text}")   
print(f"csr --> {KEYWORD in csr.text}")  
print("=" *60)

"""
    Playwright
    브라우저 자동화 통해 동적페이지 데이터 수집 지원 도구

    기본구조
    Browser 
    Context 쿠키, 캐시공간
    Page 탭
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #browser : 크롬 실행
    browser = p.chromium.launch(headless=True) #headless=True) = 창이 보이지 않음

    #context : 시크릿 창 하나. 쿠기, 캐시가 독립적으로 보관
    context = browser.new_context(locale="ko-KR",
                                  viewport={"width":1280, "height":720})
    #page : 실제로 조작하기 위한 탭 하나
    page = context.new_page()

    page.route(
        "**/*",
        lambda route: route.abort() if route.request.resource_type in {"image", "font", "media"}
                                    else route.continue_()
    )

    page.goto(f"{BASE}/csr/stocks", wait_until='domcontentloaded')

    page.wait_for_selector("tr.stock-row")

    count = page.locator("tr.stock-row").count()
    print(f" 렌더링 후 가져온 행의 개수: {count}")

    html = page.content()
    #print(f" page.content : {html}")

    items = parse_stocks(html)



    browser.close()

for data in items[:5]:
    print(f"{data['code']} : {data['name']} : {data['price']}")

"""
    * headless = False, slow_mo=1000
      화면 보면서 확인 가능
    * 스크린샷, HTML 저장
        page.screenshot(path="..../screenshot.png", full_page=True)
        open("capture.html", "w", encoding="utf-8").write(page.content())

    * 브라우저 콘솔
        page.on("console", lambda m: print(f"[BROWSER] {m.text}"))     
"""
                                      