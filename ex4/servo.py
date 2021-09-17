#coding:utf-8
import RPi.GPIO as GPIO
import time
#macro
servo=24
#settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT, initial=GPIO.LOW)
#pwm siPgnal
p=GPIO.PWM(servo, 50)#50Hz
#start of pwm
p.start(0)#duty ratio is 0%
p.ChangeDutyCycle(7.5)#0
time.sleep(1)
for i in range(3):
    p.ChangeDutyCycle(2.8)#-90
    time.sleep(1)
    p.ChangeDutyCycle(7.5)#0
    time.sleep(1)
    p.ChangeDutyCycle(13)#90
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
#cleanup
p.stop()
GPIO.cleanup()
