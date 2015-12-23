import numpy as np
import copy
def calc_nb(array, letter, light_matrix, i):
	# print "I was here", array, letter, i
	nb=0
	if array==0 and letter==0:
		# if light_matrix[array+1][letter]=="#": nb+=1
		# if light_matrix[array+1][letter+1]=="#": nb+=1
		# if light_matrix[array][letter+1]=="#": nb+=1
		nb=2
	elif array==99 and letter==0:
		# if light_matrix[array-1][letter]=="#": nb+=1
		# if light_matrix[array-1][letter-1]=="#": nb+=1
		# if light_matrix[array][letter+1]=="#": nb+=1
		nb=2
	elif array==0 and letter==99:		
		# if light_matrix[array+1][letter]=="#": nb+=1
		# if light_matrix[array+1][letter-1]=="#": nb+=1
		# if light_matrix[array][letter-1]=="#": nb+=1
		nb=2
	elif array==99 and letter==99:
		# if light_matrix[array-1][letter]=="#": nb+=1
		# if light_matrix[array-1][letter-1]=="#": nb+=1
		# if light_matrix[array][letter-1]=="#": nb+=1
		nb=2
	elif array==99:
		if light_matrix[array][letter-1]=="#": nb+=1
		if light_matrix[array][letter+1]=="#": nb+=1
		for x in range (letter-1, letter+2):
			if light_matrix[array-1][x]=="#": nb+=1
	elif array==0:
		if light_matrix[array][letter-1]=="#": nb+=1
		if light_matrix[array][letter+1]=="#": nb+=1
		for x in range (letter-1, letter+2):
			if light_matrix[array+1][x]=="#": nb+=1
	elif letter==0:
		if light_matrix[array-1][letter]=="#": nb+=1
		if light_matrix[array+1][letter]=="#": nb+=1
		for x in range (array-1, array+2):
			if light_matrix[x][letter+1]=="#": nb+=1
	elif letter==99:
		if light_matrix[array-1][letter]=="#": nb+=1
		if light_matrix[array+1][letter]=="#": nb+=1
		for x in range (array-1, array+2):
			if light_matrix[x][letter-1]=="#": nb+=1
	else:
		for x in range (array-1, array+2):
			if light_matrix[x][letter-1]=="#": nb+=1
		for x in range (array-1, array+2):
			if light_matrix[x][letter+1]=="#": nb+=1
		if light_matrix[array-1][letter]=="#": nb+=1
		if light_matrix[array+1][letter]=="#": nb+=1
	return nb 										

def main():
	light_matrix=[line for line in open("input18.txt")]
	light_matrix=map(lambda it: it.strip("\n"), light_matrix)
	i=0

	while(i is not 100):
		matrix_copy=[]
		for array in range(len(light_matrix)):
			# print len(light_matrix)
			rows=[]
			for letter in range(100):
				nb=calc_nb(array, letter, light_matrix, i)
				if light_matrix[array][letter]=="#": 
					if nb==3 or nb==2:
						rows.append('#')
					else:
						rows.append('.')		
				elif light_matrix[array][letter]==".":
					if nb==3:
						rows.append('#')
					else:
						rows.append('.')
			# print len(rows)							
			matrix_copy.append(rows)
			# row=[]		
		light_matrix=copy.deepcopy(matrix_copy)
		# print light_matrix
		i+=1
	sum=0
	for array in light_matrix:
		for letter in array:
			if letter=="#":
				sum+=1
	print sum				
main()		















