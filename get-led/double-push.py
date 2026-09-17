import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16][::-1]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0
delta = 0
pressed = 0
while True:
    delta += GPIO.input(up)
    delta -= GPIO.input(down)
    pressed = GPIO.input(up) + GPIO.input(down)
    num += delta
    if pressed == 2:
        num = 255
    num = (num + 256) % 256
    if delta:
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        delta = 0
    GPIO.output(leds, dec2bin(num))
    