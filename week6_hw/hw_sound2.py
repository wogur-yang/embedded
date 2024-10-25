# mybuzzer
import RPi.GPIO as gpio
import time

buzzer = 12

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)

p = gpio.PWM(buzzer,261)
p.start(50)

p.start(50)

try:
    while True:
        for i in range(13):
            if i == 6 or i == 10 or i == 11:
                p.start(50)
                p.ChangeFrequency(330)
                time.sleep(0.2)
                p.stop()
                time.sleep(0.1)
        
            elif i == 3 or i == 2:
                p.start(50)
                p.ChangeFrequency(440)
                time.sleep(0.2)
                p.stop()
                time.sleep(0.1)

            elif i == 12:
                p.start(50)
                p.ChangeFrequency(292)
                time.sleep(0.2)
                p.stop()
                time.sleep(0.1)

            elif i == 7:
                p.stop()
                time.sleep(0.2)
        
            else :
                p.start(50)
                p.ChangeFrequency(394)
                time.sleep(0.2)
                p.stop()
                time.sleep(0.1)
        
        p.stop()
        time.sleep(0.5)

except KeyboardInterrupt:
    pass


p.stop()
gpio.cleanup()