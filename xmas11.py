from itertools import *
def condition(input):
	# print input
	if 'i' in input or 'l' in input or 'o' in input:
		flag1=0
	else:
		flag1=1
	counter=0
	for letter in range(len(input)-2):
		if input[letter+1]==chr(ord(input[letter])+1) and input[letter+2]==chr(ord(input[letter])+2):
			counter+=1
	
	if counter>0:
		flag2=1
	else:
		flag2=0
	counter=0
	for k, g in groupby(input):
		if len(list(g))>=2:
			counter+=1

	if counter>=2:
		flag3=1
	else:
		flag3=0
	# print "I was here", flag1, flag2, flag3	

	if flag1>0 and flag2>0 and flag3>0:
		return True
	else:
		return False		

def iterate(input, num):
	# print input
	if input[num]=='z':
		input[num]='a'
		# print num-1
		iterate(input, num-1)
	else:
		input[num]=chr(ord(input[num])+1)		

def iterate_array(input):
	while(condition(input) is not True):
		iterate(input, -1)
	return input	


def main():
	input="vzbxkghb"
	array_string=list(input)
	input=''.join(iterate_array(array_string))
	print input
	# iterate(input, -1)
	# print input

main()	