#!/usr/bin/python

from gpiozero import Motor
import time

tM = Motor(17, 27)

tM.forward(1)
time.sleep(2)
tM.forward(0)
