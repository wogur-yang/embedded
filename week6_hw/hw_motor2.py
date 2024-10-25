import RPi.GPIO as gpio
import time

switch = [5, 6, 13, 19]

pwma = 18
ain1 = 22
ain2 = 27
pwmb = 23
bin1 = 25
bin2 = 24

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pwma,gpio.OUT)
gpio.setup(ain1,gpio.OUT)
gpio.setup(ain2,gpio.OUT)
gpio.setup(pwmb,gpio.OUT)
gpio.setup(bin1,gpio.OUT)
gpio.setup(bin2,gpio.OUT)

for i in range(4):
    gpio.setup(switch[i],gpio.IN,pull_up_down=gpio.PUD_DOWN)

lmotor = gpio.PWM(pwma,500)
lmotor.start(0)
rmotor = gpio.PWM(pwmb,500)
rmotor.start(0)

swValue = [0,0,0,0]
preValue = [0,0,0,0]

try:
    while True:
        for i in range(len(swValue)):
            swValue[i] = gpio.input(switch[i])

        if swValue[0] == 1:
            gpio.output(ain1,0)
            gpio.output(ain2,1)
            gpio.output(bin1,0)
            gpio.output(bin2,1)
            lmotor.ChangeDutyCycle(50)
            rmotor.ChangeDutyCycle(50)
            time.sleep(0.1)
            if preValue[0] == False:
                print("click sw1")

        elif swValue[1] == 1:
            gpio.output(ain1,0)
            gpio.output(ain2,1)
            gpio.output(bin1,0)
            gpio.output(bin2,0)
            lmotor.ChangeDutyCycle(50)
            rmotor.ChangeDutyCycle(50)
            time.sleep(0.1)
            if preValue[1] == 0:
                print("click sw2")

        elif swValue[2] == 1:
            gpio.output(ain1,0)
            gpio.output(ain2,0)
            gpio.output(bin1,0)
            gpio.output(bin2,1)
            lmotor.ChangeDutyCycle(50)
            rmotor.ChangeDutyCycle(50)
            time.sleep(0.1)
            if preValue[2] == 0:
                print("click sw3")

        elif swValue[3] == 1:
            gpio.output(ain1,1)
            gpio.output(ain2,0)
            gpio.output(bin1,1)
            gpio.output(bin2,0)
            lmotor.ChangeDutyCycle(50)
            rmotor.ChangeDutyCycle(50)
            time.sleep(0.1)
            if preValue[3] == 0:
                print("click sw4")

        elif sum(swValue) == 0:
            gpio.output(ain1,0)
            gpio.output(ain2,0)
            gpio.output(bin1,0)
            gpio.output(bin2,0)
            lmotor.ChangeDutyCycle(50)
            rmotor.ChangeDutyCycle(50)
            time.sleep(0.1)
        
        for i in range(len(swValue)):
            preValue[i] = swValue[i]



except KeyboardInterrupt:
    pass

gpio.cleanup()