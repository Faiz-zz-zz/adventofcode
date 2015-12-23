import itertools

def main():
	array=[int(line.strip("\n")) for line in open("input17.txt")]
	counting_array=[]
	counter=0
	for i in range(1, len(array)):
		for item in itertools.combinations(array, i):
			if sum(item)==150:
				counter+=1
				counting_array.append(len(item))
	
	print "part_one=", counter			
	
	min_way=min(counting_array)
	counter=0
	for i in range(1, len(array)):
		for item in itertools.combinations(array, i):
			if sum(item)==150 and len(item)==min_way:
				counter+=1
	
	print "part_two=", counter

main()	
