# Advent of code 2017 - day 2 - part 2

import csv

def solution(inputFile):
	spreadsheet = list(csv.reader(inputFile, delimiter='\t'))
	matrix = [[int(str) for str in row] for row in spreadsheet]
	def operation(acc,row): 
		functions = [(x,y) for x in enumerate(row) for y in enumerate(row)]
		for x, y in functions:
			if (x[0] != y[0] and x[1] % y[1] == 0):
				return acc + x[1] / y[1]
	return reduce(operation, matrix, 0)

inputFile = open('input.txt')

print(solution(inputFile))
