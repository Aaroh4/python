import sys

from ft_filter import ft_filter

def main():
	'''main'''
	assert len(sys.argv) == 3, "the arguments are bad"
	assert type(sys.argv[1]) == str, "the arguments are bad"
	assert type(sys.argv[2]) != int, "the arguments are bad"
	list = sys.argv[1].split(" ")
	compare = lambda word: len(word) >= int(sys.argv[2])
	newlist = ft_filter(compare, list)
	print(newlist)

if __name__ == "__main__":
	main()