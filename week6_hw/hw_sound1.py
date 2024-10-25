import RPi.GPIO as gpio
import time

buzzer = 12

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)

p = gpio.PWM(buzzer,261)
p.start(50)

list = [261, 292, 330, 349, 394, 440, 494, 523]

try:
    while True:
        p.start(50)
        for i in range(len(list)):
            p.ChangeFrequency(list[i])
            time.sleep(0.2)
        p.stop()
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

p.stop()
gpio.cleanup()