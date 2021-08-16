import time
import board
import pwmio
from adafruit_motor import servo


# Create a PWMOut object on Pin A2:
pwn_out = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a Servo object:
servo = servo.Servo(pwn_out)


# Event loop:
while True:
    # Go from 0-180 degrees, 5 degrees at a time:
    for angle in range(0, 180, 5):
        # Set the angle:
        servo.angle = angle
        # Slight delay:
        time.sleep(0.05)

    # Go from 180-0 degrees, 5 degrees at a time:
    for angle in range(180, 0, -5):
        # Set the angle:
        servo.angle = angle
        # Slight delay:
        time.sleep(0.05)
