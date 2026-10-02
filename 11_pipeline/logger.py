"""
    로깅 설정

    [단순 출력(print) 대신 로깅(logging) 사용하는 이유]
    - 레벨 구분이 없음
       DEBUG/INFO/WARNING/ERROR/CRITICAL ..로 중요도 나누기 가능
    - 화면에만 메세지가 남음
       자동으로 실행되는 프로그램에는 화면이 없어 메세지가 사라짐
    - 출력시간 직접 제시해아 함
       포맷 통해 자동 출력 가능

    [로깅 구성 요소]
    - logger : 로그를 남길 객체 . logger.info(...)
    - handler : 로그를 어디에 남길지 결정 . 
                StreamHandler(화면/표준 출력), FileHandler(파일) 
                Logger 하나에 여러 Handler 연결하면 같은 메세지 여러 곳 출력 가능
    - formatter : 출력 형식 설정. 시간/레벨/내용 형식 지정                 
"""
import logging
import os
from datetime import datetime

from config import LOG_DIR

def setup(name="pipeline", level=logging.INFO):
    """
        화면과 파일을 동시에 기록하는 로거를 만들어서 반환

        Args:
            name : 로거 이름. getLogger(name) 로 동일한 로거 반환 가능
            level : 로깅 레벨.
                DEBUG < INFO < WARNING < ERROR < CRITICAL
        Return:
        설정이 완료된 Logger 객체        
    """

    # 로깅 설정 함수
    # 로그 폴더 생성 (있으면 패스 - exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)

    # 저장될 로그 파일 설정 
    path = os.path.join(LOG_DIR, f"{datetime.now():%Y-%m-%d}.log")

    # logger 객체 생성
    logger = logging.getLogger(name)

    # 로그 레벨 설정
    logger.setLevel(level)

    # 핸들러 초기화 --> 함수(setup) 여러 번 호출 시, 핸들러가 중복되어 같은 메세지가 여러 번 출력되는 문제 방지
    logger.handlers.clear()

    # formatter : 출력 형식 지정
    fmt = logging.Formatter("%(asctime)s [%(levelname)-7s] %(message)s","%H:%M:%S")
    """
    %(asctime)s     : 로그가 기록된 시간 . 두번째 인자 (%H:%M:%S)형식으로 표시
    %(levelname)-7s : 로그 레벨 이름(DEBUG/INFO/WARNING/ERROR/CRITICAL) . -7s: 7칸 확보 후 왼쪽 정렬
    %(message)s     : 실제 로그 메세지 내용
    """

    # 핸들러를 로거에 등록
    
    # [StreamHandler] : 화면 출력용
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    # logger에 handler 연결
    logger.addHandler(console)

    # [FileHandler] : 파일 출력용
    file = logging.FileHandler(path, encoding="utf-8")
    file.setFormatter(fmt)
    # logger에 handler 연결
    logger.addHandler(file)

    return logger
