import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        GPIO.output(self.gpio_bits, dec2bin(number))
        time.sleep(self.compare_time)

    def sequential_counting_adc(self):
        int_volt = 0
        self.number_to_dac(int_volt)
        while (GPIO.input(self.comp_gpio) and int_volt < 255 - 1): # или инвертировать!!!
            int_volt += 1
            self.number_to_dac(int_volt)
        return int_volt

    def get_sc_voltage(self):
        int_volt = self.sequential_counting_adc()
        return int_volt * self.dynamic_range / 255


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.183, True) # другой dynamic_range!!!

        while True:
            volt = adc.get_sc_voltage()
            print(volt)
        
    finally:
        adc.deinit()