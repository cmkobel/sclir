'''
Motivation
* This project is perfect for playing with regex

Todo
*alignment
*color
*sqrt


'''


import sys
import re
import time
import math
wpm = int(sys.argv[1])

# text = sys.argv[2]
text = "That sounds like a device-dependent questionaoesntasontedisanothsnatoe.    If you printed to a hardcopy output device, you'll need white-out or scissors to unprint the output.  If you've printed to a display (e.g. a PC screen), there's probably a way to do a reverse linefeed and then print some blanks to overwrite whatever is already on the line.  If you'll be more specific about what you have in mind, I'll see what I can rig up.   \"Curses\" is a UNIX library to let a program be somewhat device independent while doing things on a screen  (e.g. vi).   A more-or-less portable version of it is available for Python.  See 15.11. curses - Terminal handling for character-cell displays - Python 2.7.11 documentation" #"Der var en ko"

#conversion
word_list = re.sub("[\s]", " ",  text).split()

def func(len):
    if word[-1::] == ".":
    	return 1/(wpm/60)  * (len/20 + 0.75) * 2
    elif word[-1::] == ",":
    	return 1/(wpm/60)  * (len/20 + 0.75) * 1.5
    else:
    	return 1/(wpm/60)  * (len/20 + 0.75)


print("WPM: ", wpm, end="\n\n\n")

for word in word_list:
	#skriv
	print("\t", word, end="")


	#vent
	time.sleep(func(len(word)))	# rewrite til lambda


	#slet
	sys.stdout.write("\033[K")	#slet linjen
	print("\r", end="")			#gå tilbage til start




print()




