#!/usr/bin/env python

__author__ = 'Greg Surges'

'''
    pySnakeCorral.py
    interface between OSC messages and pucktronix.snake.corrral hardware
    created 08.18.2011
    last modified 03.30.2012
    copyleft greg surges - pucktronix
    surgesg@gmail.com
    http://www.gregsurges.com/
'''

import simpleOSC 
import threading
import serial
from serial.tools.list_ports import comports
import time
import pypm

presets = []
ser = serial.Serial()

INPUT = 0
OUTPUT = 1
MidiIn = None

def print_devices(InOrOut):
	''' from test_pyportmidi.py '''
	for loop in range(pypm.CountDevices()):
		interf, name, inp, outp, opened = pypm.GetDeviceInfo(loop)
		if ((InOrOut == INPUT) & (inp == 1) |
			(InOrOut == OUTPUT) & (outp == 1)):
			print loop, name, " ",
			if (inp == 1): print "(input) ",
			else: print "(output) ",
			if (opened == 1): print "(opened)"
			else: print "(unopened)"
	print

def init_midi():
	''' prompt for and open MIDI device '''
	global MidiIn
	pypm.Initialize()	
	print_devices(INPUT)
	dev = int(raw_input("Type input number: "))
	MidiIn = pypm.Input(dev)
	print "Midi Input Opened"

def init_serial():
	''' poll serial ports, prompt user for port, open port '''
	ports = comports()
	for i, port in enumerate(ports):
		print "[" + str(i) + "]" + " " + port[0]
	port_choice = input("Select serial port: ")
	ser.baudrate = 19200
	ser.port = ports[port_choice][0]
	ser.open()
	if ser.isOpen(): print "Opened serial port: " + ser.port

def write_bytes(bytes):
	''' write bytes to serial port corresponding to a single pin being toggled '''
	ser.write(bytes)

def print_msg(addr, tags, stuff, source):
	''' just print out received data '''
	print "---"
	print "received new osc msg from %s" % OSC.getUrlStr(source)
	print "with addr : %s" % addr
	print "typetags %s" % tags
	print "data %s" % stuff
	print "---"

def pin_msg(addr, tags, stuff, source):
	''' toggle a single pin on/off '''
	# osc message should look like "/matrix/one x y state" to match max 
	if addr == '/matrix/one': chip_byte = 255
	if addr == '/matrix/two': chip_byte = 254
	x = stuff[0]
	y = stuff[1]
	state = stuff[2]
	bytes = ''.join([chr(i) for i in [chip_byte, x, y, state]]) 
	write_bytes(bytes)
	print addr, x, y, state

def load_presets():
	''' load a preset from txt file '''
	global presets
	file_name = raw_input("Enter filename for presets: ") 
	print "Loading " + file_name + "..."
	preset_file = open(file_name, 'r')
	temp_preset = []
	for line in preset_file:
		if line[0] != "*":
			temp_preset.append(line)	
		else:
			temp_preset = [line[0:8] for line in temp_preset] # remove EOL chars
			for line in temp_preset:
				print line
			presets.append(temp_preset)
			temp_preset = []

def preset_msg(addr, tags, stuff, source):
	''' respond to OSC preset msg '''
	global presets
	preset_num = stuff[1]
	which_matrix = stuff[0]
	recall_preset(preset_num, which_matrix)

def recall_preset(preset_num, which_matrix):
	''' recall a stored preset, and apply it to a given matrix '''
	global presets
	if preset_num >= len(presets): # check that preset exists and exit if not
		print "Error: Preset " + str(preset_num) + " does not exist."
		return
	if which_matrix == 0: chip_byte = 255
	if which_matrix == 1: chip_byte = 254
	cur_preset = presets[preset_num]
	print "Recalled Preset " + str(preset_num) + " on Matrix " + str(which_matrix)
	for i, row in enumerate(cur_preset):
		for j, col in enumerate(row):
			x = j
			y = i
			state = int(col)
			bytes = ''.join([chr(i) for i in [chip_byte, x, y, state]]) 
			write_bytes(bytes)

def load_msg():
	''' welcome / copyleft msg '''
	print "\n\n\n"
	print "pySnakeCorral.py"
	print "for use with pucktronix.snake.corral"
	print "copyleft 2012 pucktronix"
	print "http://www.gregsurges.com/"
	print "surgesg@gmail.com"

def process_midi():
	MidiData = MidiIn.Read(1)
	if MidiData[0][0][2] == 0: return # ignore noteoff messages
	note_num = MidiData[0][0][1]
	if note_num < 18: 
		matrix = 0
	else: 
		matrix = 1
		note_num -= 18 # offset back to 0 - 17
	recall_preset(note_num, matrix)
	
def main():
	load_msg()
	print "\n[0] Load Presets \
		\n[1] Start OSC Server"
	user_choice = input(": ")
	if user_choice == 0:
		load_presets()
		
	osc_port = input("Enter OSC Server port: ")
	address = '127.0.0.1', osc_port 
	simpleOSC.initOSCServer(address[0], address[1], 1)
	print "Server Initialized..."
	print "Listening on Port: " + str(address[1])
	simpleOSC.setOSCHandler("/print", print_msg) # adding our function
	simpleOSC.setOSCHandler("/matrix/one", pin_msg) # add msgs for matrix one 
	simpleOSC.setOSCHandler("/matrix/two", pin_msg) # add msgs for matrix two 
	simpleOSC.setOSCHandler("/matrix/preset", preset_msg) # add msgs for matrix two 
	if raw_input("Init midi? y/n: ") == "y": init_midi()
	init_serial()
	print "\nStarting OSCServer. Use ctrl-C to quit."
	# loop to allow interception of keyboard while receiving OSC
	try:
		while 1:
			time.sleep(0.1)
			while not MidiIn.Poll(): pass
			process_midi()	

	except KeyboardInterrupt:
		try:
			simpleOSC.closeOSC()
		except:
			print "Caught OSC exception"
		print "\nClosing Serial Port..."
		ser.close()

if __name__ == "__main__":
	main()
