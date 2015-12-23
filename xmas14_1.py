def main():
	reinder=dict()
	for line in open("input14.txt"):
		(fly, _, _, speed, _, _, time, _, _,_,_,_,_, rest, _)=line.split()
		reinder[fly]=map(int, [speed, time, rest, '0', '0'])
	
	lead_array=[]	
	for second in range(1, 2504):
		distance_array=[]
		for fly in reinder:
			left_time=second %(reinder[fly][1]+reinder[fly][2])
			if left_time>reinder[fly][1] or left_time==0:
				reinder[fly][3]+=0
			else:
				reinder[fly][3]+=reinder[fly][0]
			distance_array.append(reinder[fly][3])	
		# print distance_array			
		for fly in reinder:
			if reinder[fly][3]==max(distance_array):
				reinder[fly][4]+=1
	for fly in reinder:
		lead_array.append(reinder[fly][4])
	# print lead_array		
	print max(lead_array)			
main()		