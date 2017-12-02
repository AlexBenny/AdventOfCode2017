# Advent of code 2017 - 1st December - part 2

def solution(input):

	inputList = map((lambda ch: int(ch)), list(input))

	v1 = inputList[:len(inputList)/2]
	v2 = inputList[len(inputList)/2:]

	result = 0

	for n1, n2 in zip(v1,v2):
		result += (0, n1)[n1 == n2]

	return result * 2


#input = "123123"
input = open('input.txt').read()

print(solution(input))
