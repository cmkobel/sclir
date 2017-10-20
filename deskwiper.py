

class clir:


	# Simple debug printer (for code reuse).
	def debug_print(self, *inputs):
		if self.debug is True:
			print(inputs)
			
			
	def __init__(self) #, source, destination, deadline=2*86400, debug=True):
		pass

	



	
	
	
	# Run the routine of moving the files.
	# def run(self):
# 		os.chdir(self.source) # For good measure
# 		self.debug_print("starts at: ", time.time())
# 
# 		for file in self.candidates():
# 			self.debug_print('moving', file)
# 			os.rename(file, os.path.join(self.destination, file))


