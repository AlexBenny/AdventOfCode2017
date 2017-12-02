# Advent of code 2017 - 1st December


def december1(input):

	inputList = map((lambda ch: int(ch)), list(input))

	result = 0
	oldN = inputList[-1]

	for n in inputList:
		result += (0, oldN)[oldN == n]
		oldN = n

	return result


input = open('input.txt').read()

print(december1(input))
