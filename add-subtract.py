
import sys
import numpy

def main():

	''' Read in mathematical relationship as value - desired operation - value and evaluate, works for add,sub,dev'''
	input1 = sys.argv[1]
	operation = sys.argv[2]
	input2 = sys.argv[3]

	print eval(input1 + operation + input2)

main()