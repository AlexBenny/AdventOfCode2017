# Advent of code 2017 - day 2

import csv

def solution(inputFile):
	spreadsheet = list(csv.reader(inputStr, delimiter='\t'))
	matrix = [[int(str) for str in row] for row in spreadsheet]
	def operation(acc,row): 
		return acc + max(row) - min(row)
	return reduce(operation, matrix, 0)

inputFile = open('input.txt')

print(solution(inputFile))
