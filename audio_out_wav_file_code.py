import time
import board
import digitalio
from audiocore import WaveFile


# Handle import errors for different boards:
try:
    from audioio import AudioOut
    
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    
    except ImportError:
        pass


button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

wav_file = open('Sample001.wav', 'rb')
wave = WaveFile(wav_file)
audio = AudioOut(board.A0)


# Event loop:
while True:
    audio.play(wave)
    
    # Do other stuff while playing the audio file:
    t = time.monotonic()
    while ((time.monotonic() - t) < 6):
        pass
    
    audio.pause()
    print("Press button to continue!")
    
    while button.value:
        pass

    audio.resume()
    while audio.playing:
        pass
    
    print("All done!")
