#coding:utf-8
import RPi.GPIO as GPIO
import time
#macro
button=25
led=24
#settngs
GPIO.setmode(GPIO.BCM) #buttun25->GPIO25
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
print("push button")
while True:
    btn=GPIO.input(button)#read the statement of buttun
    if btn == True:
        GPIO.output(led,1) #turn on
        time.sleep(7)      #1 secound wait
        GPIO.output(led,0) #turn off
        time.sleep(1)
        break
#finish
GPIO.cleanup()
