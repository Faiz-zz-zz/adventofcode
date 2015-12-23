def main():
	ingred=dict()
	for line in open("input15.txt"):
		(name, _, quant1, _, quant2, _, quant3, _, quant4, _, quant5)=line.split()
		ingred[name.strip(":")]=map(int,map(lambda it: it.strip(','), [quant1, quant2, quant3, quant4, quant5]))
	print ingred
	print 1*ingred["Sprinkles"][0]+2*ingred["Butterscotch"][0]+3*ingred["Chocolate"][0]+4*ingred["Candy"][0]	
	score=[]	
	for spr in range(0, 101):
		for but in range(0, 101):
			for choc in range(0, 101):
				for can in range(0, 101):
					if spr+but+choc+can==100 and ((spr+but)*3+(choc+can)*8)==500:
						if can>=but*5 or 2*spr+3*but>=5*choc or choc>=5*can:
							continue
						else:	
							a=spr*ingred["Sprinkles"][0]+but*ingred["Butterscotch"][0]+choc*ingred["Chocolate"][0]+can*ingred["Candy"][0]			
							b=spr*ingred["Sprinkles"][1]+but*ingred["Butterscotch"][1]+choc*ingred["Chocolate"][1]+can*ingred["Candy"][1]
							c=spr*ingred["Sprinkles"][2]+but*ingred["Butterscotch"][2]+choc*ingred["Chocolate"][2]+can*ingred["Candy"][2]
							d=spr*ingred["Sprinkles"][3]+but*ingred["Butterscotch"][3]+choc*ingred["Chocolate"][3]+can*ingred["Candy"][3]
							# e=spr*ingred["Sprinkles"][4]+but*ingred["Butterscotch"][4]+choc*ingred["Chocolate"][4]+can*ingred["Candy"][4]
							print a, b, c, d
							# if a*b*c*d*e==13324953600: print "herrrrrrrrrrrreeeeeeeeeeeeeeeeeee"
							# print a*b*c*d*e	
							score.append(a*b*c*d)
	# print a, b, c, d, e
	print max(score)				
main()						
# [(59,1,34,6),(59,1,35,5)]