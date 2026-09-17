import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

state = 0
period = 1.0 # s

while True:
    GPIO.output(led, state)
    state = not state # i understand that false == 0, true == 1
    time.sleep(period)