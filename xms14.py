def main():
	reinder=dict()
	for line in open("input14.txt"):
		(fly, _, _, speed, _, _, time, _, _,_,_,_,_, rest, _)=line.split()
		reinder[fly]=map(int, [speed, time, rest, '0'])
	distance_array=[]	
	for fly in reinder:
		left_time=2503 %(reinder[fly][1]+reinder[fly][2])
		if left_time>reinder[fly][1]:
			reinder[fly][3]+=((2503/(reinder[fly][1]+reinder[fly][2]))+1)*reinder[fly][0]*reinder[fly][1]
		else:
			reinder[fly][3]+=(2503/(reinder[fly][1]+reinder[fly][2]))*reinder[fly][0]*reinder[fly][1]+left_time*reinder[fly][0]
		distance_array.append(reinder[fly][3])
		print distance_array
	print max(distance_array)		
main()		