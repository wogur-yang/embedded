import RPi.GPIO as gpio
import time

switch = 5
buzzer = 12

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)
gpio.setup(switch,gpio.IN,pull_up_down=gpio.PUD_DOWN)

previous = 0
p = gpio.PWM(buzzer,261)
sw1Value = 0

try:
    while True:
        sw1Value = gpio.input(switch)
        if sw1Value - previous == 1:
            p.start(50)
            p.ChangeFrequency(261)
            time.sleep(0.5)
            p.stop()
            time.sleep(0.1)
        previous = sw1Value    

except KeyboardInterrupt:
    pass


gpio.cleanup()