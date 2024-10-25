import RPi.GPIO as gpio
import time

switch = 5

gpio.setmode(gpio.BCM)
gpio.setup(switch,gpio.IN,pull_up_down=gpio.PUD_DOWN)

count = 0

try:
    while True:
        swValue = gpio.input(switch)
        if swValue == 1:
            count += 1
            print("click", count)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

gpio.cleanup()