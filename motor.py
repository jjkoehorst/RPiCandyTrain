# This script is to control two motors with commands from the keyboard. We use the L293D chip for the motor control. The enabling is done via PWM, we use PIN #21/27 and PIN #18 from the GPIO as PWM pins.
# For IN1, IN2, IN3 and IN4 we use the pins #4, #17, #23 and #24.
# YOU NEED TO RUN THE SCRIPT AS SUDO!
# The commands to steer the motors look like f/r 0..9 f/r 0..9 for example f8r9 (and press ENTER)
# The first two digits are for the first motor (connected to OUT1 and OUT2), f meaning clockwise, r meaning counter-clockwise, the number between 0 and 9 indicating the speed.
# The same principle is for the last two digits and the second motor.
# You can end the program by typing q (and ENTER)

import RPi.GPIO as io
# mode is set to BCM numbering
io.setmode(io.BCM)

# name the pins used
in1_pin = 4
in2_pin = 17
in3_pin = 23
in4_pin = 24
pwm1_pin = 27 # this number depends on your version of the Pi. If it's Model A it should be 21
pwm2_pin = 18

# set the pins as output pins
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(pwm1_pin, io.OUT)
io.setup(pwm2_pin, io.OUT)

# set and start the PWM pins
p1 = io.PWM(pwm1_pin, 0.5)
p2 = io.PWM(pwm2_pin, 0.5)
p1.start(11)
p2.start(11)

# methods for turning the motors clockwise and counter-clockwise for both motors seperately
def clockwise1():
	io.output(in1_pin, True)
	io.output(in2_pin, False)

def counter_clockwise1():
	io.output(in1_pin, False)
	io.output(in2_pin, True)

def clockwise2():
	io.output(in3_pin, True)
	io.output(in4_pin, False)

def counter_clockwise2():
	io.output(in3_pin, False)
	io.output(in4_pin,True)

# main loop, asking for input and calling the methods above to steer
while True:
	# Wait for input
	cmd = raw_input("Command, f/r 0..9 f/r 0..9, E.g. f5r9 :")
	# stop if input is q
	if cmd[0]=="q":
		break

	# get directions
	direction1 = cmd[0]
	direction2 = cmd[2]
	# set directions
	if direction1 == "f":
		clockwise1()
	else:
		counter_clockwise1()

	if direction2 == "f":
		clockwise2()
	else:
		counter_clockwise2()
	
	# get speed
	speed1 = int(cmd[1]) * 11
	speed2 = int(cmd[3]) * 11
	# set speed
	p1.ChangeDutyCycle(speed1) 
	p2.ChangeDutyCycle(speed2)

# Just to make sure it left the loop
print "Engines stopped"

# stop the PWM
p1.stop()
p2.stop()

# clean up the GPIO
io.cleanup()
