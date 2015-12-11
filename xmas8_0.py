print sum(len(s[:-1]) - len(eval(s)) for s in open('input8.txt'))
print sum(2+s.count('\\')+s.count('"') for s in open('input8.txt'))
for s in open("input8.txt"):
	print eval(s), len(eval(s))
	print s, len(s), 
	print 
