filename = sys.argv[1]
import sys
def process(s):
	ans = 0
	for c in s:
		if c.isalpha():
			if c.islower():
				ans += ord(c) - 96
			else:
 				ans += ord(c) - 65 + 27
	return ans

with open(filename) as f:
	data = f.read().strip()
	print(process(data))
