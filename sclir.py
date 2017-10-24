

import sys
import re
import time
import math
import pyperclip

class sclir:

	'''
		~ Todo ~ 
	
	* blink ord ved linjeskift?
	* keyboard controls
		* venstre: Gå en sætning tilbage
		* højre: ?
		* op/ned: juster hastighed
		* q quit
	* use curses?
		* brug farver

	'''

	def __init__(self,
		wps = 8,
		text="No text", 
		acceleration = 1/11, 
		debug = False):
		self.wps = int(wps)
		self.text = pyperclip.paste().replace("\n", " ⏎ ")
		self.acceleration = acceleration
		self.debug = debug

		# As the standard word lenght is usually 5, we can find the intersect
		self.lin_offset = 1 - 5 * self.acceleration

		# The time to show a standard word (5 letters)
		self.time = 1/(self.wps)


	# debug printer
	def debug_print(self, *inputs):
		if self.debug is True:
			print(inputs)
			return


	def scale(self, word):
		self.len = len(word)
		end = word[-1::]

		if end == ".": self.multiplier = 2
		elif end == "!": self.multiplier = 2
		elif end == "⏎": self.multiplier = 3
		elif end == "?": self.multiplier = 2
		elif end == ":": self.multiplier = 2
		elif end == ",": self.multiplier = 1.2
		else: self.multiplier = 1

		return self.time * (self.len * self.acceleration + self.lin_offset) * self.multiplier


	def whitespace(self, len):

		n = int(10 - int(math.sqrt(len)*1.16-1))

		product = ""

		for i in range(0, n):
			product += " "

		return product


	def progress(self):
		pass


	def del_n_lines(self, n):
		for i in range(0, n):
			sys.stdout.write("\033[F") #back to previous line
			sys.stdout.write("\033[K") #clear line




	def run(self):

		# put teksten ind i en liste
		self.word_list = re.sub("[\s]", " ", self.text).split()
		
		# skriv titlen på teksten ...
		print("  Text:\t", end="")
		for i in range (0, 5):
			print (self.word_list[i], end=" ")
		print("...")

		# skriv hastigheden
		print(" Speed:\t", self.wps, "w/s ~", int((len(self.word_list) / self.wps / 60)), "min")

		# initialiser counteren der skal bruges til at holde styr på progressen
		counter = 0

		print()
		print()
		print()
		print()

		print("           |")


		for word in self.word_list:
			counter += 1

			self.del_n_lines(5)

			# progress
			print("Progr.:\t", int(3*(counter/len(self.word_list))-0.001)+1, "/ 3\n")
			print("           |")
			print(self.whitespace(len(word)), word)
			print("           |")
			
			time.sleep(self.scale(word))

		print()



