from ..formats.wave import wave_out

DELAY = 3

def echo_out(file):
    print(f"{file} 플레이 {DELAY}초 적용")
    wave_out(file)