import sys
filename = sys.argv[1]
def reduce(s):
	for i in range(len(s)-1):
		if (s[i].isalpha()) and s[i+1].isdigit() or s[i].isdigit() and (s[i+1].isalpha()):
			return (True, s[:i]+s[i+2:])
	return (False, "")

with open(filename) as f:
	data = f.read().splitlines()
	s = 0
	for line in data:
		current = line
		poss = True
		while poss:
			poss, reduced = reduce(current)
			if poss:
				current = reduced
		s += len(current)
	print(s)