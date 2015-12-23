def main():
	detail={"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}
	for line in open("input16.txt"):
		(_, number, name1, quant1, name2, quant2, name3, quant3)=line.split()
		if detail[name1.strip(':')]==int(quant1.strip(",")) and detail[name2.strip(':')]==int(quant2.strip(",")) and detail[name3.strip(':')]==int(quant3.strip(",")):
			print "partone "+number.strip(":")		
main()
