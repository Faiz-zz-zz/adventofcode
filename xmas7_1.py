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
		if array[0]=='b':	
			print value[varArray.index(array[0])], value[varArray.index(array[4])]
		value[varArray.index(array[4])]=value[varArray.index(array[0])]>>int(array[2])
		if array[0]=='b':	
			print value[varArray.index(array[0])], value[varArray.index(array[4])]

		return 1
	else:
		return 0	
						
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
	realArray=[]
	varArray=[]
	file=open("input7_1.txt")
	data=file.readlines()
	for line in data:
		varDict(line, varArray)
	varSet=set(varArray)
	varArray=removeElement(varSet)
	for line in data:
		array=[]
		array=line.split()
		realArray.append(array)
	value=[]
	for i in range(339):
		value.append("faiz")
	value[varArray.index('b')]=46065
	
	i=0

	while(value[varArray.index('a')]=="faiz"):
		for array in realArray:	
			if array[1]=='RSHIFT':
				flag=0
				flag=rightShiftOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
			elif array[1]=='LSHIFT':
				flag=0
				leftShiftOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
			elif array[1]=='->':
				flag=0
				inputOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
			elif array[0]=='NOT':
				flag=0
				notOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
			elif array[1]=='OR':
				flag=0
				orOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
			elif array[1]=='AND':
				flag=0
				andOp(array,value, varArray)
				if flag==1:
					realArray.remove(array)
		print value[varArray.index('b')]		
		i+=1

	print "answer=",value[varArray.index('a')]

main()	