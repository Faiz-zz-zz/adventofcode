def restrictedDouble(input):
	counter=0
	for letter in range(len(input)-1):
		if (input[letter]=='a' and input[letter+1]=='b') or (input[letter]=='c' and input[letter+1]=='d') or (input[letter]=='p' and input[letter+1]=='q') or (input[letter]=='x' and input[letter+1]=='y'):
			counter+=1
	if counter>0:
		return 0
	else:
		return 1			

def doubleLetter(input):
	counter=0
	for letter in range(len(input)-1):
		if input[letter]==input[letter+1]:
			counter+=1
	if counter>=1:
		return 1
	else:
		return 0			

def vowels(input):
	counter=0
	for letter in range(len(input)):
		if input[letter]=='a' or input[letter]=='e' or input[letter]=='i' or input[letter]=='o'or input[letter]=='u':
			counter+=1
	if counter>=3:
		return 1
	else:
		return 0				

def first_check(input):
	flag1=vowels(input)
	flag2=doubleLetter(input)
	flag3=restrictedDouble(input)
	print flag1, flag2, flag3
	return flag1 and flag2 and flag3

def main():
	file=open("input5.txt")
	data=file.readlines()
	sum=0
	for line in data:
		sum=sum+first_check(line)
	print sum	

main()	
