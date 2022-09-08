import sys
import getopt

def full_name2():
	first_name = None
	last_name = None
	hellpp = None
	argv = sys.argv[1:]

	try:
		opts, args = getopt.getopt(argv, "f:l:h:")
	
	except:
		print("Error")

	for opt, arg in opts:
		if opt in ['-f']:
			first_name = arg
		elif opt in ['-l']:
			last_name = arg
		elif opt in ['-h']:
			hellpp = arg
	
	

	print( first_name +" " + last_name +" "+ hellpp )

full_name2()
