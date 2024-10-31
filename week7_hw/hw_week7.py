import serial
import time
import threading
import RPi.GPIO as gpio

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

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData=""

def serial_write():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def go():
    gpio.output(ain1,0)
    gpio.output(ain2,1)
    gpio.output(bin1,0)
    gpio.output(bin2,1)
    lmotor.ChangeDutyCycle(50)
    rmotor.ChangeDutyCycle(50)
    time.sleep(1.0)

def back():
    gpio.output(ain1,1)
    gpio.output(ain2,0)
    gpio.output(bin1,1)
    gpio.output(bin2,0)
    lmotor.ChangeDutyCycle(50)
    rmotor.ChangeDutyCycle(50)
    time.sleep(1.0)

def right():
    gpio.output(ain1,0)
    gpio.output(ain2,1)
    gpio.output(bin1,0)
    gpio.output(bin2,0)
    lmotor.ChangeDutyCycle(50)
    rmotor.ChangeDutyCycle(50)
    time.sleep(1.0)

def left():
    gpio.output(ain1,0)
    gpio.output(ain2,0)
    gpio.output(bin1,0)
    gpio.output(bin2,1)
    lmotor.ChangeDutyCycle(50)
    rmotor.ChangeDutyCycle(50)
    time.sleep(1.0)

def stop():
    gpio.output(ain1,0)
    gpio.output(ain2,0)
    gpio.output(bin1,0)
    gpio.output(bin2,0)
    lmotor.ChangeDutyCycle(50)
    rmotor.ChangeDutyCycle(50)
    time.sleep(1.0)

def main():
    global gData
    try:
        while True:
            if gData.find("B0") >= 0:
                go()
                gData = ""
                print("ok go")
                
            elif gData.find("B5") >= 0:
                back()
                gData = ""
                print("ok back")
                
            elif gData.find("B1") >= 0:
                left()
                gData = ""
                print("ok left")

            elif gData.find("B3") >= 0:
                right()
                gData = ""
                print("ok right")
            
            elif gData.find("B2") >= 0:
                stop()
                gData = ""
                print("ok stop")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    task1 = threading.Thread(target = serial_write)
    task1.start()
    main()
    gpio.cleanup()
    bleSerial.close()