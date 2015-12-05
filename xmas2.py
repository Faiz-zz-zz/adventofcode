def toList(str):
	t=str.split('x')
	listInt=[]
	for x in t:
		listInt.append(int(x))
	print "\n"
	return process(listInt)

def	process(listInt):
	minValue=min(listInt)
	sum=2*(listInt[0]*listInt[1]+listInt[1]*listInt[2]+listInt[0]*listInt[2])+min(listInt[0]*listInt[1], listInt[1]*listInt[2], listInt[0]*listInt[2])
	return sum

def toListforRibbon(str):
	t=str.split('x')
	listInt=[]
	for x in t:
		listInt.append(int(x))
	print "\n"
	return processforRibbon(listInt)

def	processforRibbon(listInt):
	minValue=min(listInt)
	sum=2*min(listInt[0]+listInt[1], listInt[1]+listInt[2], listInt[0]+listInt[2])+listInt[0]*listInt[1]*listInt[2]
	return sum

def main():
	answer=0
	answerRibbon=0
	file=open("input.txt")
	data=file.readlines()
	for line in data:
		answer=answer+toList(line)
		answerRibbon=answerRibbon+toListforRibbon(line)
	print answer, " ", answerRibbon


main()

