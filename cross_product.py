'''
Simon Orlovsky
4 April 2015

This this is a function that finds the cross product of two vectors in three-space
'''

def cross(vector1, vector2):
	x = vector1[1]*vector2[2]-vector1[2]*vector2[1]
	y = vector1[0]*vector2[2]-vector1[2]*vector2[0]
	z = vector1[0]*vector2[1]-vector1[1]*vector2[0]
	return (x,-y,z)

def main():
	vector1 = (1,1,-1)
	vector2 = (1,2,2)
	print cross(vector1, vector2)

main()

