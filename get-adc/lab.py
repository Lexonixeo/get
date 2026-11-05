import sys
sys.stdout = open("res2.txt", 'w')

import RPi.GPIO as GPIO
import mcp3021_driver as mcp
import adc_plot as plott
import time

max_voltage = 5.227

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT, initial = 0)

adc = mcp.MCP3021(max_voltage)
voltages = []
times = []
duration = 30.0

print("v t")
try:
    time_start = time.time()
    GPIO.output(14, 1)
    while time.time() - time_start < duration:
        v = adc.get_voltage()
        t = time.time() - time_start
        print(v, t)
        times += [t]
        voltages += [v]
    GPIO.output(14, 0)
    while time.time() - time_start < 2 * duration:
        v = adc.get_voltage()
        t = time.time() - time_start
        print(v, t)
        times += [t]
        voltages += [v]
    plott.plot_voltage_vs_time(times, voltages, max_voltage)
    #plott.plot_sampling_period_hist(times)
finally:
    adc.deinit()
    GPIO.output(14, 0)
    GPIO.cleanup()