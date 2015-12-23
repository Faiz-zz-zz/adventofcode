def main():
	detail={"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}
	for line in open("input16.txt"):
		(_, number, name1, quant1, name2, quant2, name3, quant3)=line.split()
		flag1=0
		flag2=0
		flag3=0
		if name1.strip(':')=="cats" or name1.strip(':')=='trees' or name1.strip(':')=='pomeranians' or name1.strip(':')=='goldfish':
			if name1.strip(':')=="cats" or name1.strip(':')=='trees':
				if detail[name1.strip(':')]<int(quant1.strip(",")):
					flag1=1
			elif name1.strip(':')=='pomeranians' or name1.strip(':')=='goldfish':
				if detail[name1.strip(':')]>int(quant1.strip(",")):
					flag1=1
		
		else:	
			if detail[name1.strip(':')]==int(quant1.strip(",")):
				# if number.strip(":")=='40':
					# "I was here"
				flag1=1

		if name2.strip(':')=="cats" or name2.strip(':')=='trees' or name2.strip(':')=='pomeranians' or name2.strip(':')=='goldfish':
			if name2.strip(':')=="cats" or name2.strip(':')=='trees':
				if detail[name2.strip(':')]<int(quant2.strip(",")):
					flag2=1
			elif name2.strip(':')=='pomeranians' or name2.strip(':')=='goldfish':
				if detail[name2.strip(':')]>int(quant2.strip(",")):
					flag2=1
		else:	
			if detail[name2.strip(':')]==int(quant2.strip(",")):
				flag2=1

		if name3.strip(':')=="cats" or name3.strip(':')=='trees' or name3.strip(':')=='pomeranians' or name3.strip(':')=='goldfish':
			if name3.strip(':')=="cats" or name3.strip(':')=='trees':
				if detail[name3.strip(':')]<int(quant3.strip(",")):
					flag3=1
			elif name3.strip(':')=='pomeranians' or name3.strip(':')=='goldfish':
				if detail[name3.strip(':')]>int(quant3.strip(",")):
					flag3=1
		else:	
			if detail[name3.strip(':')]==int(quant3.strip(",")):
				flag3=1	
		# print number.strip(":"),flag1, flag2, flag3, flag1+flag2+flag3, name1.strip(':'), int(quant1.strip(","))
		if flag1>0 and flag2>0 and flag3>0:
			print "parttwo "+number.strip(":")				
		
				
						 	
main()