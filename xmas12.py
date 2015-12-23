import re
import json

def hook(obj):
	if "red" in obj.values(): return {}
	else: return obj


def main():
	file=open("input12.txt")
	data=file.read()
	# array = re.findall(r'[\d]+', data)
	neg_array=re.findall(r'-?[\d]+', data)
	number_sum=0
	for element in neg_array:
		number_sum+=int(element)
	print number_sum
	stuff=str(json.loads(data, object_hook=hook))
	# print "Sum of all numbers 2:", sum(map(int, re.findall(r'-?[\d]+', stuff)))
	print stuff

main()	