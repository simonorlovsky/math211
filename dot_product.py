'''
Simon Orlovsky
4 April 2015

This is a function that finds the dot product of two vectors.

TO DO:
Come back to this to test
'''

def dot(vector1, vector2):
	if len(vector1) == len(vector2):
		value = 0
		for i in range(len(vector1)):
			value = value + vector1[i]*vector2[i]
		return value
	else:
		return "Invalid input"


