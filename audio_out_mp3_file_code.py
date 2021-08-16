import board
import digitalio

from audiomp3 import MP3Decoder


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

# Create a list of mp3 files that will be played in order:
mp3_files = ["Sample001.mp3", "Sample2.mp3"]

# Specify an mp3 file when creating the decoder:
mp3 = open(mp3_files[0], 'rb')
decoder = MP3Decoder(mp3)
audio = AudioOut(board.A0)


# Event loop:
while True:
    for filename in mp3_files:
        # Updating the .file property of the existing decoder
        # helps avoid running out of memory (MemoryError exception)
        decoder.file = open(filename, "rb")
        audio.play(decoder)
        print("playing", filename)

        # This allows you to do other things while the audio plays!
        while audio.playing:
            pass
            print("Press button to continue!")

        while button.value:
            pass
