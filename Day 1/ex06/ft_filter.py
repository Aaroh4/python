import sys

def ft_filter(first, second):
	'''Remake of the filter function'''
	list = [x for x in second if (first(x) == True)]
	return (list)
