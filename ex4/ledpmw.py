#coding:utf-8
import RPi.GPIO as GPIO
import time
#led GPIO pin
led = 24
#settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
#pwm signal
p = GPIO.PWM(led, 1000)
#start of pwm
p.start(0)
dutyratio = 0
for i in range(3):
    for j in range(5):
        dutyratio += 10
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)
    for j in range(5):
        dutyratio -= 10
        p.ChangeDutyCycle(dutyratio)
        time.sleep(1)
#clean up
p.stop()
GPIO.cleanup()