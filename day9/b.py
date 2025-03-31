import sys
filename = sys.argv[1]
def transaction(users, s, d, m):
	t = min(users[s], m)
	users[s] -= t
	users[d] += t
with open(filename) as f:
	counts, trans = f.read().split("\n\n")
	users = {}
	for c in counts.splitlines():
		print(c)
		u, balance = c.split(" HAS ")
		users[u] = int(balance)
	for t in trans.splitlines():
		s,d = t.split(" TO ")
		s = s[5:]
		d, m = d.split(" AMT ")
		transaction(users, s, d, int(m))
	l = users.values()
	print(sum(sorted(l, reverse=True)[:3]))
	
