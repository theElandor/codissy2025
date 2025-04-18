import sys
f1 = sys.argv[1]
f2 = sys.argv[2]
data1 = open(f1).read()
data2 = open(f2).read()
s1 = set()
s2 = set()
for line in data1.splitlines():
	s1.add(line)
for line in data2.splitlines():
	s2.add(line)
print(f"Stuff present in {f1} and not in {f2}")
for item in s1:
	if item not in s2:
		print(item)