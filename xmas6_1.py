# light_grid=[[0 for x in range(1000)] for x in range(1000)]

def call_summation(light_grid):
	light=sum(map(sum, light_grid))
	print light 
		

def grid_operation(array, switch_state, light_grid):
    for i in range(array[0], array[2]+1):
    	for j in range(array[1], array[3]+1):
    		if switch_state==1:
    				light_grid[i][j]+=1
    		elif switch_state==0:
    				light_grid[i][j]+=2
    		elif switch_state==2 and light_grid[i][j]>0:
    				light_grid[i][j]-=1									
    			

def make_array_of_numbers(input, light_grid):
	array=input.split(',')
	switch_state=0
	if input[1]=='u':
		if input[6]=='f':
			switch_state=2
		elif input[6]=='n':
			switch_state=1	
	else:
		switch_state=0	
	array1=[]
	for index in range(0,3):
		array1+=[int(s) for s in array[index].split() if s.isdigit()]
	grid_operation(array1, switch_state, light_grid)	

def main():
	light_grid=[[0 for x in range(1000)] for x in range(1000)]
	file=open("input6.txt")
	data=file.readlines()
	for line in data:
		make_array_of_numbers(line, light_grid)
	call_summation(light_grid)	
main()	