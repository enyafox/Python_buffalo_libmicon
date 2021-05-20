#!/usr/bin/python3

##simple example of polling one button and taking an action if it is held down.
import libmicon, time

while True:
	test = libmicon.micon_api("/dev/ttyS1")
	state=int.from_bytes(test.send_read_cmd(0x36),byteorder="big")
	##print button number
	print(state)
	test.port.close()
	time.sleep(0.5)
quit()


"""What you could do is use this to read a simple number, for example, the TS-XL models, unpressed is 31, the power button is 30, 
the function button is 29, display is 17 and the hidden reset button is 23.
You can use this to build a script using that code above,

import libmicon, time, os

press_time=0
poll_speed=0.5 ##currently this is fast as we can reliably poll
tickcnt=0

while True:
	test = libmicon.micon_api("/dev/ttyS1")
	state=int.from_bytes(test.send_read_cmd(0x36),byteorder="big")
	##if button held down start counting
	if state == 30:
		tickcnt=tickcnt +1
		if tickcnt > (press_time/poll_speed):
			print("Function Button Pressed")
			tickcnt=0

	##reset counter if released
	else:
		tickcnt=0

	test.port.close()
	##currently this is fast as we can reliably poll
	time.sleep(poll_speed)
quit()"""
