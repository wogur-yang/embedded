import RPi.GPIO as gpio
import time

buzzer = 12
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)

switch = [5, 6, 13, 19]
for i in range(4):
    gpio.setup(switch[i],gpio.IN,pull_up_down=gpio.PUD_DOWN)

p = gpio.PWM(buzzer,261)
swValue = [0,0,0,0]

try:
    while True:
        for i in range(len(switch)):
            swValue[i] = gpio.input(switch[i])
        if swValue[0] == 1:
            p.start(50)
            p.ChangeFrequency(261)
            time.sleep(0.2)
            p.stop()
            time.sleep(0.1)
        elif swValue[1] == 1:
            p.start(50)
            p.ChangeFrequency(330)
            time.sleep(0.2)
            p.stop()
            time.sleep(0.1)
        elif swValue[2] == 1:
            p.start(50)
            p.ChangeFrequency(394)
            time.sleep(0.2)
            p.stop()
            time.sleep(0.1)
        elif swValue[3] == 1:
            p.start(50)
            p.ChangeFrequency(440)
            time.sleep(0.2)
            p.stop()
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
gpio.cleanup()