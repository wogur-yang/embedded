import RPi.GPIO as gpio
import time
import math

switch = 5

gpio.setmode(gpio.BCM)
gpio.setup(switch,gpio.IN,pull_up_down=gpio.PUD_DOWN)

count = 0
prevalue = False

try:
    while True:
        sw1Value = gpio.input(switch)
        if sw1Value - prevalue == 1:
            count += 1
            print("click", count)  
        prevalue = sw1Value    
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

gpio.cleanup()