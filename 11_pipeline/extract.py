"""
    Extract :데이터 수집해 원본 그대로 보관

    - 하지 않은 것 : 데이터 정제(가공)
"""
import time
import pandas as pd
import requests

from config import (KHLAB_BASE, raw_prices_path, ENCODING, SOURCE, MAX_PAGES, PAGE_SIZE, DELAY, TIMEOUT)

# HTTP 요청 헤더
# => 누가 어떤 목적으로 요청하는 지 정보 담아둠
# - USER-AGENT : 요청 보내는 클라이언트 이름 
# - X-....: 비표준 헤더 설정
HEADERS = {
    "User-Agent": "KHLab-Pipeline/1.0(교육용 실습)",
    "X-Student-Id": "260611",
}

def from_api(logger, max_pages=MAX_PAGES):
    """
    API 호출해 데이터 수집
    KH-Lab API에서 데이터 수집해 반환

    Return: (rows, failed)
    rows : 응답 데이터 list[dlct] 변환
    failed : 응답 실패한 페이지 번호 목록
    """
    rows, failed = [], []

    with requests.Session() as s:
        s.headers.update(HEADERS)

        for page in range(1, max_pages + 1):

            try:
                resp = s.get(f"{KHLAB_BASE}/api/v1/companies", params={"page": page, "limit": PAGE_SIZE}, timeout=TIMEOUT)

            except requests.RequestException as e:
                logger.warning(f" 페이지 {page} 요청 실패: {type(e).__name__}")
                failed.append(page)
                continue

            # 상태 코드 확인 . 200이 아닌 경우 파싱 작업 패스
            if resp.status_code != 200:
                logger.warning(f" page {page} 상태 코드 {resp.status_code}")
                failed.append(page)
                continue

            body = resp.json() #응답 본문(JSON) -> dict 변환
            items = body.get("items") or []

            if not items:
                # 응답 본문이 비어있을 경우, 더 이상 데이터 없음
                logger.info(f" page {page} 0건 - 종료")
                break

            rows.extend(items)
            logger.info(f" page {page} {len(items)}건 (누적 {len(rows)}건)")

            # 요청 간 대기 시간 설정
            time.sleep(DELAY)

    if failed:
        logger.warning(f" 실패 페이지: {failed}")   

    return rows, failed
     

def from_csv(logger, path=None):
    """
    CSV 파일 읽어 데이터 수집
    API 통신이 불안정하거나, 오프라인 상태일 때 사용

    Args:
        path : CSV 파일 경로. 생략 시 config에 저장된 경로 사용

    Return: (rows, failed)
    rows : 수집된 데이터 목록
    failed : 응답 실패한 페이지 목록이나 페이지 정보 없어 빈 리스트 반환

    """

    # path가 생략되었을 경우(None) 원본 파일 경로 (raw_prices_path()로 가본 경로 사용

    # 저장된 데이터 그대로 유지해 읽어온 후 (-로그 기록) dict 변환
    path = path or raw_prices_path()

    df = pd.read_csv(path, encoding=ENCODING, dtype=str, keep_default_na=False)
    logger.info(f"  {path} 로부터 {len(df):,}행 읽음")

    #dict 변환
    return df.to_dict("records"), []