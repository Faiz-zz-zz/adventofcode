def repeatedPair(input):
	counter=0
	for letter in range(len(input)-3):
		for search in range(letter+2, len(input)-1):
			if (input[letter]==input[search] and input[letter+1]==input[search+1]):
				counter+=1
				print "here", letter+1 , search+1, input[letter],input[letter+1]+" and "+input[search], input[search+1], input
	return counter			

def repeatLetter(input):
	counter=0
	for letter in range(len(input)-2):
		# print input[letter], input[letter+2]
		if input[letter]==input[letter+2]:
			counter+=1
	if counter>=1:
		return 1
	else:
		return 0			
				

def first_check(input):
	flag1=repeatLetter(input)
	flag2=repeatedPair(input)
	print flag1, flag2
	return (flag1>0 and flag2>0)

def main():
	file=open("input5.txt")
	data=file.readlines()
	sum=0
	for line in data:
		sum=sum+first_check(line)
	print sum	

main()	
