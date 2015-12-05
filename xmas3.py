a=[[False for x in range(200)]for x in range(200)]

def sumfunction(counter):
	print a[counter[0]][counter[1]]
	if(a[counter[0]][counter[1]]!=True):
		a[counter[0]][counter[1]]=True
		return 1
	else:
		return 0	

def main():
	file=open("input3.txt")
	data=file.read()
	counter=[100, 100]
	answer=1
	for letter in data:
		print answer
		if (letter=='^'):
			counter[0]+=1
			answer=answer+sumfunction(counter)

		elif (letter=='v'):
			counter[0]-=1
			answer=answer+sumfunction(counter)

		elif (letter=='>'):
			counter[1]+=1
			answer=answer+sumfunction(counter)

		elif (letter=='<'):
			counter[1]-=1
			answer=answer+sumfunction(counter)
	print answer		

main()						