import itertools
# def inputOp():

inputArray=[]
notArray=[]
orArray=[]
leftShiftArray=[]
rightShiftArray=[]
andArray=[]

def inputOp(array, value, varArray):
	if array[0].isdigit():
		value[varArray.index(array[2])]=int(array[0])
		return 1
	elif value[varArray.index(array[0])]!="faiz":
		value[varArray.index(array[2])]=value[varArray.index(array[0])]
		return 1
	else:
		return 0	


def andOp(array, value, varArray):
	if array[0].isdigit() and array[2].isdigit()==False:
		if value[varArray.index(array[2])]!="faiz":
			value[varArray.index(array[4])]=value[varArray.index(array[2])] & int(array[0])
			return 1
	elif array[0].isdigit()==False and array[2].isdigit():
		if value[varArray.index(array[0])]!="faiz":
			value[varArray.index(array[4])]=value[varArray.index(array[0])] & int(array[2])
			return 1
	elif value[varArray.index(array[0])]!="faiz" and value[varArray.index(array[2])]!="faiz":
			value[varArray.index(array[4])]=value[varArray.index(array[0])] & value[varArray.index(array[2])]
			return 1
	else:
		return 0			
					


def notOp(array, value, varArray):
	if array[1].isdigit():
		value[varArray.index(array[3])]= ~int(array[1])
		return 1
	elif value[varArray.index(array[1])]!="faiz":
			value[varArray.index(array[3])]=~value[varArray.index(array[1])]
			return 1
	else:
		return 0
				

def orOp(array, value, varArray):
	# if array[0].isdigit() and array[2].isdigit()==False:
		# if value[varArray.index(array[2])]!="faiz"
			# value[varArray.index(array[4])]=value(varArray.index[array[2])] | int(array[0])
	# elif array[0].isdigit()==False and array[2].isdigit():
		# if value[varArray.index(array[0])]!="faiz"
			# value[varArray.index(array[4])]=value[varArray.index(array[0])] | int(array[2])
	# else:
	if 	value[varArray.index(array[0])]!="faiz" and value[varArray.index(array[2])]!="faiz":
		value[varArray.index(array[4])]=value[varArray.index(array[0])] | value[varArray.index(array[2])]
		return 1
	else:
		return 0		

def leftShiftOp(array, value, varArray):
	if 	value[varArray.index(array[0])]!="faiz":
		value[varArray.index(array[4])]=value[varArray.index(array[0])]<<int(array[2])
		return 1
	else:
		return 0	


def rightShiftOp(array, value, varArray):
	if 	value[varArray.index(array[0])]!="faiz":
		# print array[0], value[varArray.index(array[0])]
		value[varArray.index(array[4])]=value[varArray.index(array[0])]>>int(array[2])
		return 1
	else:
		return 0	


def checkOp(line):
	array=[]
	array=line.split()
	if array[1]=='RSHIFT':
		rightShiftArray.append(array)
	elif array[1]=='LSHIFT':
		leftShiftArray.append(array)
	elif array[1]=='->':
		inputArray.append(array)
	elif array[0]=='NOT':
		notArray.append(array)
	elif array[1]=='OR':
		orArray.append(array)
	elif array[1]=='AND':
		andArray.append(array)					


def removeElement(varSet):
	# varSet.remove(" ")
	varSet.remove("->")
	varSet.remove("AND")
	varSet.remove("OR")
	varSet.remove("RSHIFT")
	varSet.remove("NOT")
	varSet.remove("LSHIFT")
	array=list(varSet)
	arrayNoNumbers=[item for item in array if not item.isdigit()]
	return arrayNoNumbers

def varDict(line, varArray):
	varArray+= line.split()

def main():

	varArray=[]
	file=open("input7.txt")
	data=file.readlines()
	for line in data:
		varDict(line, varArray)
	varSet=set(varArray)
	varArray=removeElement(varSet)
	for line in data:
		checkOp(line)
	value=[]
	for i in range(339):
		value.append("faiz")
	value[varArray.index('b')]=46065
	# print value
	i=0
	while(value[varArray.index('a')]=="faiz"):
					
		for array in rightShiftArray:
			flagInput=0	
			flagInput=rightShiftOp(array, value, varArray)
			if flagInput==1:
				rightShiftArray.remove(array)

		for array in inputArray:
			flagInput=0	
			flagInput=inputOp(array, value, varArray)
			if flagInput==1:
				inputArray.remove(array)
		for array in notArray:
			flagInput=0	
			flagInput=notOp(array, value, varArray)
			if flagInput==1:
				notArray.remove(array)

		for array in andArray:
			flagInput=0	
			flagInput=andOp(array, value, varArray)
			if flagInput==1:
				andArray.remove(array)	

		for array in leftShiftArray:
			flagInput=0	
			flagInput=leftShiftOp(array, value, varArray)
			if flagInput==1:
				leftShiftArray.remove(array)						
		
		for array in orArray:
			flagInput=0	
			flagInput=orOp(array, value, varArray)
			if flagInput==1:
				orArray.remove(array)
		print value[varArray.index('b')]

		for array in inputArray:
			flagInput=0	
			flagInput=inputOp(array, value, varArray)
			if flagInput==1:
				inputArray.remove(array)		
		i+=1		

	print "answer=",value[varArray.index('a')]

main()	