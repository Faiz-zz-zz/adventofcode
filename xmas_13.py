from itertools import permutations
import copy

def main():
	people=[]
	for line in open("input13.txt"):
		people.append(line.split()[0])	
	intex=list(set(people))
	intex.append("faiz")	
	people={'Mallory': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'Eric': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'George': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'Carol': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'Frank': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'Bob': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'Alice': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'David': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'faiz':[0, 0, 0, 0, 0, 0, 0, 0, 0]}
	for line in open("input13.txt"):
		# print line
		(person, _, sign, value, _, _, _, _, _, _, person1)=line.split()
		print person, sign, value, person1
		if sign=='gain':
			array=people.get(person)
			array[intex.index(person1.strip("."))]+=int(value)
		elif sign=='lose':
			array=people.get(person)
			array[intex.index(person1.strip("."))]-=int(value)
	value=[]
	for seating in permutations(people):
		total=0
		for arrange in range(len(seating)-1):
			total+=people[seating[arrange]][intex.index(seating[arrange+1])]+people[seating[arrange+1]][intex.index(seating[arrange])]
		total+=people[seating[0]][intex.index(seating[-1])]+people[seating[-1]][intex.index(seating[0])]
		value.append(total)

	print max(value)	
main()