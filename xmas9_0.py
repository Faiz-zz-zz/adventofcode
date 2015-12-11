def update_distance(distance_array,place_array, line):
	array=[]
	array=line.split()
	distance_array[place_array.index(array[0])][place_array.index(array[2])]=int(array[4])

def make_set(line, place_array):
	array=[]
	array=line.split()
	place_array.append(array[0])
	place_array.append(array[2])

def solution():
	sum=0
	while(sum(distance_array!=9999*8*8)):
		value=0
		value= min(map(min, distance_array))
		sum+=value
		for x in range(len(place_array)):
			distance_array[]
			

def main():
	file=open("input9.txt")
	data=file.readlines()
	place_array=[]
	for line in data:
		make_set(line,place_array)
	place_set=set(place_array)
	place_array=list(place_set)
	distance_array=[[9999 for x in range(len(place_array))] for x in range(len(place_array))]
	for line in data:
		update_distance(distance_array, place_array, line)
	print place_array
	for row in distance_array:	
		print row

main()	