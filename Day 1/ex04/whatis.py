import sys

if (len(sys.argv) < 2):
	exit (1)
assert len(sys.argv) == 2, "more than one argument is provided"
assert sys.argv[1].lstrip("-").isdigit(), "argument is not an integer"
if (int(sys.argv[1]) % 2 == 0):
	print("I'm Even.")
else:
	print("I'm Odd.")