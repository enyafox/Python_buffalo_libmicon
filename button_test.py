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

press_time=2
poll_speed=0.5 ##currently this is fast as we can reliably poll
tickcnt=0

while True:
	test = libmicon.micon_api("/dev/ttyS1")
	state=int.from_bytes(test.send_read_cmd(0x36),byteorder="big")
	##if button held down start counting
	if state == 30:
		tickcnt=tickcnt +1
		if tickcnt > (press_time/poll_speed):
			test.set_lcd_buffer(0x90,"Shutting Down!!"," ")
			test.cmd_force_lcd_disp(libmicon.lcd_disp_buffer0)
			test.send_write_cmd(1,libmicon.lcd_set_dispitem,0x20)
			test.set_lcd_color(libmicon.LCD_COLOR_RED)
			test.set_lcd_brightness(libmicon.LCD_BRIGHT_FULL)
			test.cmd_sound(libmicon.BZ_MUSIC1)
			test.port.close() ##if we do something other than shutdown we'd probably skip this
			os.system('shutdown -h 0')
			tickcnt=0

	##reset counter if released
	else:
		tickcnt=0

	test.port.close()
	##currently this is fast as we can reliably poll
	time.sleep(poll_speed)
quit()"""
