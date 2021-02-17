#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes
from gpiozero import Motor
import time

remote = InputDevice('/dev/input/event0')

#aft/forward + starboard/port
asMotor = Motor(27,17)
apMotor = Motor(26,19)
fsMotor = Motor(16,12)
fpMotor = Motor(21,20)

for event in remote.read_loop():
	if event.type == ecodes.EV_KEY:
		print(event.code)
		print(event.value)
	if event.code == 128:
		break
	if event.code == 3 and (event.value == 1 or event.value == 2):
		asMotor.forward(1)
		apMotor.forward(1)
		fsMotor.forward(1)
		fpMotor.forward(1)
	elif event.code == 3 and event.value == 0:
		asMotor.forward(0)
		apMotor.forward(0)
		fsMotor.forward(0)
		fpMotor.forward(0)
#tM.forward(1)
#time.sleep(2)
#tM.forward(0)
