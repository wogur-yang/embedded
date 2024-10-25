import RPi.GPIO as gpio
import time

switch = 5

gpio.setmode(gpio.BCM)
gpio.setup(switch,gpio.IN,pull_up_down=gpio.PUD_DOWN)

try:
    while True:  
        sw1Value = gpio.input(switch)
        if sw1Value == 1:
            print("click")
        time.sleep(0.1)


except KeyboardInterrupt:
    pass

gpio.cleanup()

