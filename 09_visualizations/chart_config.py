import platform
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

_DEFAULT_FONT={
    "Windows" : ["Malgun Gothic"],
    "Darwin" : ["AppleGothic"],
}

_FALLBACK = ["NanumGothic", "Noto Sans CJK KR", "Noto Sans CJK JP", "IPAGothic"]

def find_Korean_font():
    installed = {f.name for f in font_manager.fontManager.ttflist}
    for name in _DEFAULT_FONT.get(platform.system(), []) + _FALLBACK:
        if name in installed:
            return name
    return None    

OUTPUT_DIR = Path(__file__).with_name("output")

def out(name):
    #output/ 폴더 내의 파일 경로 반환
    OUTPUT_DIR.mkdir(exist_ok=True)
    return OUTPUT_DIR / name

def saved_files():
    #output/ 폴더에 저장된 파일 이름 목록 반환
    OUTPUT_DIR.mkdir(exist_ok=True)

    #iterdir() : 폴더 안을 하나씩 돌면서 반환
    return sorted(p.name for p in OUTPUT_DIR.iterdir() if p.is_file())


#=====
#설정
#=====
def setup(theme=True):
    """
    한글 폰트 설정, 마이너스 기호 설정
    seaborn 테마 설정 먼저 해야함

    Args: 
        theme : seaborn 테마 설정 여부
    """
    if theme:
        #seaborn 테마 설정
        import seaborn as sns
        sns.set_theme(style="whitegrid")

    # 한글 폰트 설정
    font = find_Korean_font()
    if font:
        #plt.rcParams : 전역 기본값 표(dict)
        plt.rcParams["font.family"] = font

    # 마이너스 기호 설정
    plt.rcParams["axes.unicode_minus"] = False

    # 그래프 저장 시 축 라벨이 잘리는 현상 해결
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["savefig.bbox"] = "tight"



