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
	if event.code == 128: #KEY_STOP END PROGRAM
		break
	if event.code == 3 and (event.value == 1 or event.value == 2): #KEY_2 FORWARD
		asMotor.forward(1)
		apMotor.forward(1)
		fsMotor.forward(1)
		fpMotor.forward(1)
	elif event.code == 3 and event.value == 0: #KEY_2 STOP
		asMotor.forward(0)
		apMotor.forward(0)
		fsMotor.forward(0)
		fpMotor.forward(0)
	elif event.code == 9 and (event.value == 1 or event.value == 2): #KEY_8 BACKWARD
		asMotor.backward(1)
		apMotor.backward(1)
		fsMotor.backward(1)
		fpMotor.backward(1)
	elif event.code == 9 and event.value == 0: #KEY_8 STOP
		asMotor.backward(0)
		apMotor.backward(0)
		fsMotor.backward(0)
		fpMotor.backward(0)
	elif event.code == 5 and (event.value == 1 or event.value == 2): #KEY_5 STRAFE LEFT
		asMotor.forward(1)
		apMotor.backward(1)
		fsMotor.backward(1)
		fpMotor.forward(1)
	elif event.code == 5 and event.value == 0: #KEY_5 STOP
		asMotor.forward(0)
		apMotor.backward(0)
		fsMotor.backward(0)
		fpMotor.forward(0)
	elif event.code == 7 and (event.value == 1 or event.value == 2): #KEY_7 STRAFE RIGHT
		asMotor.backward(1)
		apMotor.forward(1)
		fsMotor.forward(1)
		fpMotor.backward(1)
	elif event.code == 7 and event.value == 0: #KEY_7 STOP
		asMotor.backward(0)
		apMotor.forward(0)
		fsMotor.forward(0)
		fpMotor.backward(0)
