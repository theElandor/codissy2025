import sys
filename = sys.argv[1]
with open(filename) as f:
	data = f.read().splitlines()
	s = 0
	for line in data:
		for c in line:
			if c.isalpha():
				s += 1
	print(s)