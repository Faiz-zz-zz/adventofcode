import json


file=open("input12.txt")
data=file.read()
print json.dumps(data, sort_keys=True, indent=5, separators=(',', ':'))
# print json.dumps(data, sort_keys=True, indent=5, separators=(',', ':'))