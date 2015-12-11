from itertools import groupby

def sumto(array, index):
	answer=0
	for x in range(index):
		answer=answer+array[x]
	return answer	

def process(input,num ):
	for i in xrange(num):
		input = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input)])
	return input	

def main():
	input="1113122113"
	print len(process(input, 100))

main()