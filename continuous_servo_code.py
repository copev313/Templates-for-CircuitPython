import time
import board
import pwmio
from adafruit_motor import servo


# Create PWMOut object on Pin A2:
pwm_out = pwmio.PWMOut(board.A2, frequency=50)


# Create Servo object:
servo = servo.ContinuousServo(pwm_out)


# Event Loop:
while True:
    print("Going forward")
    servo.throttle = 1.0
    time.sleep(2)

    print("Stop!")
    servo.throttle = 0.0
    time.sleep(2)

    print("Going backward")
    servo.throttle = -1.0
    time.sleep(2)

    print("Stop!")
    servo.throttle = 0.0
    time.sleep(2)
