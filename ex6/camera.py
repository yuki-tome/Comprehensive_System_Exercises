#coding: utf-8
import webiopi
import os
import datetime
#save directory
SAVEDIR = '/home/pi/ex6'
@webiopi.macro
def camera(no):
    #filename
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    #taking a picture
    command = 'fswebcam -r 320x240 -d /dev/video0 ' + filename
    os.system(command)
    #writing to disk cache
    os.system('sync')
#camera('1')
@webiopi.macro
def datetimeget():
    now = datetime.datetime.now()
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    #datetime = month + "." + day + " " + hour + ":" + minute + ":" + second
return month + "月" + day + "日" + hour + "時" + minute + "分" + second + "秒"
