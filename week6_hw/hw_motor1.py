import RPi.GPIO as gpio
import time

pwma = 18
ain1 = 22
ain2 = 27
pwmb = 23
bin1 = 25
bin2 = 24
switch = [5, 6, 13, 19]

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pwma,gpio.OUT)
gpio.setup(ain1,gpio.OUT)
gpio.setup(ain2,gpio.OUT)
gpio.setup(pwmb,gpio.OUT)
gpio.setup(bin1,gpio.OUT)
gpio.setup(bin2,gpio.OUT)

lmotor = gpio.PWM(pwma,500)
lmotor.start(0)
rmotor = gpio.PWM(pwmb,500)
rmotor.start(0)

try:
    while True:
        gpio.output(ain1,0)
        gpio.output(ain2,1)
        gpio.output(bin1,0)
        gpio.output(bin2,1)
        lmotor.ChangeDutyCycle(50)
        rmotor.ChangeDutyCycle(50)
        time.sleep(1.0)

        gpio.output(ain1,0)
        gpio.output(ain2,0)
        gpio.output(bin1,0)
        gpio.output(bin2,0)
        lmotor.ChangeDutyCycle(50)
        rmotor.ChangeDutyCycle(50)
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

gpio.cleanup()