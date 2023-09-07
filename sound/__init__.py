#package init file:여기있는 요소들을 네임스페이스 이름으로 참조 가능해짐
from .formats.wave import wave_out as wave

def music_play(file):
    print(f"{file}을 연주합니다.")