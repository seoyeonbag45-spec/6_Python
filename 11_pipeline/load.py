"""
    Load. 데이터 DB에 적재(저장)

    - 하지 않는 것 : 정제(가공)
    - upsert 사용해 데이터 있으면 UPDATE, 없으면 INSERT
    - 대용량 한 번에 처리 X 
"""
import time

from config import connect, CHUNK_SIZE

COLS = ["code", "date", "open", "high", "low", "close", "volume", "change", "changeRate"]

def _quote(c):

    return f'"{c}"' if c in ("date", "change", "changeRate") else c

# SQL 조각
COL_SQL = ",".join(_quote(c) for c in COLS) 

#위치 기반 바인드 변수 문자열
PH = ",".join([f":{i+1}" for i in range(len(COLS))])

#MERGE INTO 사용 시 별칭 지정 문자열
MERGE_USING = "," .join(f":{i+1} AS {_quote(c)}" for i, c in enumerate)

# 실행할 쿼리문
UPSERT = """
MERGE INTO daily_price dst
USING (SELECT {MERGE_USING} FROM dual) src
ON (dst.code = src.code AND dst."date" = src."date")
WHEN MATCHED THEN
    UPDATE SET dst.open = src.open,
               dst.high = src.high,
               dst.low = src.low,
               dst.close = src.close,
               dst.volume = src.volume,
               dst."change" = src."change",
               dst."changeRate" = src."changeRate"
WHEN NOT MATCHED THEN
    INSERT ({COL_SQL})
    VALUES (src.code, src."date", src.open, src.high, src.low, src.close, src.volume, src."change", src."changeRate")

"""
def _row_count(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*)FROM daily_price")
        return cur.fetchone()[0]

def to_db(df, logger, chunk=CHUNK_SIZE):
    """
    upsert로 적재하고 (신규 건수, 갱신 건수, 소요 시간) 반환
    """
    data = df[COLS].astype(object).where(df[COLS].notna(), None)
    rows = [tuple(r) for r in data.itertuples(index=False)]


    conn = connect()
    start = time.perf_counter()

    before = _row_count(conn)

    try:

        for i in range(0, len(rows), chunk):
            part = rows[i:i+chunk]

            with conn.cursor() as cur:
                cur.executemany(UPSERT, part)
            conn.commit()

    except Exception:
        conn.rollback()
        logger.warning(f" 적재 실패({i} ~ {i+chunk-1})")
        raise  
    finally:
        conn.close()

    conn2 = connect()
    after = _row_count(conn2)
    conn2.close()       

    inserted = after - before
    updated = len(rows) - inserted 
    t = time.perf_counter() - start

    logger.info(f" 적재 완료 - 신규ㅣ {inserted}건, 갱신:{updated}건 ({t})")
    return inserted, updated, t 


def verify(df, logger):
    """
        적재 후 검증  결과 반환

        [검증 항목 - (df, db)]
        - 전체 행 수
        - 종목 코드 수
        - 종가 총합
        - 날짜 최소
        - 날짜 최대

    """
    pass
