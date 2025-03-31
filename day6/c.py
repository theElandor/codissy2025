import sys
filename = sys.argv[1]
def convert(c):
	if c.islower():
		return ord(c) - 96
	else:
		return ord(c) - 65 + 27

def process_prev(prev):	
	prev *= 2
	prev -= 5
	if 1 <= prev <= 52:
		return prev
	elif prev < 1:
		while not(1 <= prev <= 52):
			prev += 52
		return prev
	elif prev > 52:
		while not(1 <= prev <= 52):
			prev -= 52
		return prev

def find(i, s):
	if s[i].isalpha():
		return convert(s[i])
	elif s[i-1].isalpha():
		prev = convert(s[i-1])
		return process_prev(prev)
	else:
		prev = find(i-1, s)
		return process_prev(prev)

with open(filename) as f:
	data = f.read().strip()
	ans = 0
	for i in range(len(data)):
		ans += find(i, data)
	print(ans)
