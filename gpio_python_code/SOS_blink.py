#!/usr/bin/python
# import libraries
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # set pin numbering system to bcm
# setup our output pins
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

for x in range(0, 3):
  print("lights on")
  GPIO.output(17,GPIO.HIGH)
  GPIO.output(27,GPIO.HIGH)
  sleep(.5) # sleep 1 second
 # turn leds off
  print("lights off")
  GPIO.output(17,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)
  sleep(0.5) # sleep 1 second
  x += 1

for x in range(0, 3):
  print("lights on")
  GPIO.output(17,GPIO.HIGH)
  GPIO.output(27,GPIO.HIGH)
  sleep(1.5) # sleep 1 second
 # turn leds off
  print("lights off")
  GPIO.output(17,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)
  sleep(0.5) # sleep 1 second
  x += 1
  
for x in range(0, 3):
  print("lights on")
  GPIO.output(17,GPIO.HIGH)
  GPIO.output(27,GPIO.HIGH)
  sleep(.5) # sleep 1 second
 # turn leds off
  print("lights off")
  GPIO.output(17,GPIO.LOW)
  GPIO.output(27,GPIO.LOW)
  sleep(0.5) # sleep 1 second
  x += 1