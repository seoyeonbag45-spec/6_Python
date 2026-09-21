"""
    공통 변수 (설정 항목)
"""
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# / : 경로 연결

ENCODING = "utf-8-sig"

def path(name):
    """
        data 폴더 안의 파일 경로 반환
    """
    return DATA_DIR / name