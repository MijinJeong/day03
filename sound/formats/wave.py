SUPPORT_FORMAT = ('wave',)
SAMPLING = 128 #kbps
CHANNEL = 'STEREO'
BITRATE = 44 #KHz

def wave_out(file):
    print(f"{file} 플레이, {SAMPLING}bps, {BITRATE}KHz, {CHANNEL}")