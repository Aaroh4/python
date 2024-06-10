import sys


def countChars(inputstring):
	'''Counts all the necessary chars'''
	charcount = 0
	spaccount = 0
	punccount = 0
	uppercount = 0
	downcount = 0
	digicount = 0

	for index in range(0, len(inputstring)):
		if (inputstring[index].isspace()):
			spaccount += 1
		elif (inputstring[index] in "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"):
			punccount += 1
		elif (inputstring[index].isupper()):
			uppercount += 1
		elif (inputstring[index].islower()):
			downcount += 1
		elif (inputstring[index].isdigit()):
			digicount += 1
	return (uppercount, downcount, punccount, spaccount, digicount, len(inputstring))


def main():
	'''main'''
	assert len(sys.argv) < 3, "more than one argument is provided"
	if (len(sys.argv) < 2):
		userinput = input("What is the text to count?\n")
	else:
		userinput = sys.argv[1]
	list = countChars(userinput)
	print("The text contains", list[5], "chracters:")
	print(list[0], "upper letters")
	print(list[1], "lower letters")
	print(list[2], "punctuation marks")
	print(list[3], "spaces marks")
	print(list[4], "digits")


if __name__ == "__main__":
	main()
