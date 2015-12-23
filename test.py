def func():
	input1=3600000
	house=[0 for x in range(1, input1*10)]
	flag=0
	for i in range(1, input1+1):
		# print i
		for j in range(i, input1+1, i):
			house[j] += i*10
			# print j
	for i in range(input1):
	 if house[i]>=input1*10:
	 	return i		

num=func()
print num				