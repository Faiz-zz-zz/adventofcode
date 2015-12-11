from itertools import *
input="aaaddsdsssfffggg"
for k, g in groupby(input):
	print k,  "equals ", list(g)