#program for pumping 200ml water using a peristaltic pump

motor1=21
import RPi,GPIO as GPIO # import RPi. GPIO module
import time
GPIO.setmode(GPIO.BCM) #choose BCM or board
GPIO.setup(motor1,GPIO.OUT) #set a port or pin as an output
while True:
    GPIO.output(motor1, True)
    time.sleep(200)
    GPIO.output(motor1, False)
    time.sleep(2000)
