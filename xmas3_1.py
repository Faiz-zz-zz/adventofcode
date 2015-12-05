a=[[False for x in range(1000)]for x in range(1000)]

def sumfunction(counter):
	if(a[counter[0]][counter[1]]!=True):
		a[counter[0]][counter[1]]=True
		return 1
	else:
		return 0	

def main():
	file=open("input3.txt")
	data=file.read()
	counter=[500, 500]
	counter_robo=[500, 500]
	answer=0
	track=1
	for letter in data:

		if (track%2==1):
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
		
		if (track%2==0):
			if (letter=='^'):
				counter_robo[0]+=1
				answer=answer+sumfunction(counter_robo)

			elif (letter=='v'):
				counter_robo[0]-=1
				answer=answer+sumfunction(counter_robo)

			elif (letter=='>'):
				counter_robo[1]+=1
				answer=answer+sumfunction(counter_robo)

			elif (letter=='<'):
				counter_robo[1]-=1
				answer=answer+sumfunction(counter_robo)	
		track+=1		
	print answer		

main()						