import hashlib

def check(string, number):
	checker=hashlib.md5(string).hexdigest()
	# print checker[0:6]=="00000", number, checker[0:5]
	if checker[0:6]=="000000":
		print number
		return 0
	else:
		return 1


def inputfunc(string):
	i=0
	flag=1
	while(flag==1):
		process=string+str(i)
		flag=check(process, i)
		i+=1

def main():
	input="yzbqklnj"
	inputfunc(input)
main()