#!/usr/bin/python

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

loop_count = 0

#define a function called morsecode
def morsecode ():

 for loop_count in range(0, 50):
  print("beeep fast")
  GPIO.output(22,GPIO.HIGH)
  sleep(.5)
 
  print("beeep slow")
  GPIO.output(22,GPIO.HIGH)
  sleep(1.5)
  
  print("beeep fast")
  GPIO.output(22,GPIO.HIGH)
  sleep(.5)
  loop_count +=1
  

os.system("clear")
print ("Morse Code")

morsecode()
