'''
Simon Orlovsky
4 April 2015

This program will calculate the equation of a plane in the following cases:

1. Given point and a normal vector
2. Given three points
'''
from dot_product import dot
from cross_product import cross

def find_equation(point, normal_vector):
	d = dot(point, normal_vector)
	equation = str(normal_vector[0])+"x"+"+"+str(normal_vector[1])+"y"+"+"+str(normal_vector[2])+"z"+"="+str(d)
	return equation

def three_points(P, Q, R):
	PQ = (Q[0]-P[0], Q[1]-P[1], Q[2]-P[2])
	PR = (R[0]-P[0], R[1]-P[1], R[2]-P[2])
	normal_vector = cross(PQ, PR)



def main():
	point = (3,1,0)
	normal_vector = (3,2,-5)
	print find_equation(point, normal_vector)

main()