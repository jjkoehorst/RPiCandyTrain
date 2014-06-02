# This script is to control two motors with the navigation keys, using the L293D chip for the motor control. 
# The enabling is done via PWM, use PIN #21/27 and PIN #18 from the GPIO as PWM pins.
# For IN1, IN2, IN3 and IN4 use the pins #4, #17, #23 and #24.
# YOU NEED TO RUN THE SCRIPT AS SUDO!
# The motors are controlled with the navigation keys and stopped with the space bar using the curses library for python. For each key press it changes the angle by 
# 10 degrees to the negative (left) or to positive (right), minimal and maximal angle is +-90 
# The motor connected to IN1 and IN2 should be the right motor, the other the left one. If the motor turns backwards when you 
# press up, you need to change the cables.
# You can end the program by typing q.
# While running it prints out what key is pressed, the current angle and speed of right and left engine, respectively

import curses
import RPi.GPIO as io

# GPIO mode is set to BCM numbering
io.setmode(io.BCM)

# name the pins used
# right motor
in1_pin = 4
in2_pin = 17
# left motor
in3_pin = 23
in4_pin = 24
# right
pwmright_pin = 27 # this number depends on your version of the Pi. If it's Model A it should be 21
# left
pwmleft_pin = 18

# set the pins as output pins
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(pwmright_pin, io.OUT)
io.setup(pwmleft_pin, io.OUT)

# set and start the PWM pins
p_right = io.PWM(pwmright_pin, 50)
p_left = io.PWM(pwmleft_pin, 50)
p_right.start(11)
p_left.start(11)


# methods for turning the motors forwards and backwards for both motors seperately
def forwards_right():
	io.output(in1_pin, True)
	io.output(in2_pin, False)

def backwards_right():
	io.output(in1_pin, False)
	io.output(in2_pin, True)

def forwards_left():
	io.output(in3_pin, True)
	io.output(in4_pin, False)

def backwards_left():
	io.output(in3_pin, False)
	io.output(in4_pin,True)

def stop():
	io.output(in1_pin, False)
	io.output(in2_pin, False)
	io.output(in3_pin, False)
	io.output(in4_pin, False)

def move_on_keys(stdscr):
	# set the angle to zero in the beginning
	angle = 0
	# main loop, waiting for input and calling the methods above to steer
	while True:
		# Wait for input
		cmd = stdscr.getch()
		# stop if input is q
		if cmd == ord('q'):
			break
		elif cmd == curses.KEY_LEFT:
			# print out what it's doing (just to control if it's working)
			stdscr.addstr('left')
			forwards_right()
			forwards_left()
			if angle > -90:
				angle -= 10
			stdscr.addstr(str(angle)) 
		elif cmd == curses.KEY_RIGHT:
			# print out what it's doing (just to control if it's working)
			stdscr.addstr('right')
			forwards_left()
			forwards_right()
			if angle < 90:
				angle += 10 
			stdscr.addstr(str(angle)) 
		elif cmd == curses.KEY_UP:
			# print out what it's doing (just to control if it's working)
			stdscr.addstr('up')
			forwards_left()
			forwards_right()
			angle = 0
			stdscr.addstr(str(angle)) 
		elif cmd == curses.KEY_DOWN:
			# print out what it's doing (just to control if it's working)
			stdscr.addstr('down')
			backwards_left()
			backwards_right()
			angle = 0
			stdscr.addstr(str(angle)) 
		elif cmd == ord(' '):
			# print out what it's doing (just to control if it's working)
			stdscr.addstr('stop')
			stop()

		# set speed according to the angle, but maximum 100 (more is not possible)
		speed_right = min(100,100 - angle)
		speed_left = min(100,100 + angle)
		# print out the speed
		stdscr.addstr(str(speed_right))
		stdscr.addstr(str(speed_left))
		p_right.ChangeDutyCycle(speed_right) 
		p_left.ChangeDutyCycle(speed_left)

# This initialises curses and starts the method above. The wrapper() function takes care about handling exceptions and quitting 
# curses properly
curses.wrapper(move_on_keys)
# Just to make sure it left the loop
print "Engines stopped"

# stop the PWM
p_right.stop()
p_left.stop()

# clean up the GPIO
io.cleanup()
