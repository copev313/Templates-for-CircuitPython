import time
import array
import math
import digitalio
from audiocore import RawSample


# Catch errors from lack of support:
try:
    from audioio import AudioOut

except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut

    except ImportError:
        pass


button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

# Change up/down to adjust volume:
tone_volume = 0.25
# Change the tone frequency to adjust pitch/Hz:
tone_freq = 440
length = 8000 // tone_freq


# Generate sine wave:
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(
        1 + math.sin(math.pi * 2 * i / length) * tone_volume * (2 ** 15 - 1)
    )


audio = AudioOut(board.A0)
# Create sound sample with the sine wave:
sine_wave_sample = RawSample(sine_wave)

while True:
    if not button.value:
        # Play the tone:
        audio.play(sine_wave_sample, loop=True)
        # Wait a bit:
        time.sleep(1)
        # Stop the tone:
        audio.stop()
