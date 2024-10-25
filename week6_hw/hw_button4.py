import RPi.GPIO as gpio
import time

switch = [5, 6, 13, 19]

gpio.setmode(gpio.BCM)
for i in range(4):
    gpio.setup(switch[i],gpio.IN,pull_up_down=gpio.PUD_DOWN)

count=[0, 0, 0, 0]
swValue = [0, 0, 0, 0]
preValue = [0, 0, 0, 0]

try:
    while True:
        for i in range(len(switch)):
            swValue[i] = gpio.input(switch[i])
        if swValue[0] - preValue[0] == 1:
            count[0] += 1
            print("sw1 click : ", count[0])
        if swValue[1] - preValue[1] == 1:
            count[1] += 1
            print("sw2 click : ", count[1])
        if swValue[2] - preValue[2] == 1:
            count[2] += 1
            print("sw3 click : ", count[2])
        if swValue[3] - preValue[3] == 1:
            count[3] += 1
            print("sw4 click : ", count[3])
        for i in range(len(switch)):
            preValue[i] = gpio.input(switch[i])
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

gpio.cleanup()
