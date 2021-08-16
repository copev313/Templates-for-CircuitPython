import time
import board
from digitalio import DigitalInOut, Direction, Pull


# Set up our LEDs:
led = DigitalInOut(board.LED)

led.direction = Direction.OUTPUT

# For Gemma M0, Trinket M0, Metro M0 Express, ItsyBitsy M0 Express, Itsy M4 Express, QT Py M0
switch = DigitalInOut(board.D2)
# switch = DigitalInOut(board.D5) # For Feather M0 Express, Feather M4 Express
# switch = DigitalInOut(board.D7) # For Circuit Playground Express

switch.direction = Direction.INPUT
switch.pull = Pull.UP


while True:
    if switch.value:
        led.value = False
    else:
        led.value = True
        
    # Set delay:
    time.sleep(0.1)

