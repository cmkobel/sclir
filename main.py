import sys
from sclir import sclir

if __name__ == "__main__":

	try:
		object = sclir(sys.argv[1])
	except IndexError:
		object = sclir(10)

	object.run()

    