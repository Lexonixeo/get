import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200) # nu = 200 Hz
duty = 0.0 # zapolnenie, %
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    #pwm.ChangeDutyCycle(2 ** duty / (2 ** 100.0) * 100.0)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0