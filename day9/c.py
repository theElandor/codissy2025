import sys
from collections import deque
filename = sys.argv[1]
def receive(users, debts, receiver, money):	
	while money > 0:
		try:
			user, db = debts[receiver].popleft()
		except:
			break
		if money >= db:
			receive(users, debts, user, db)
			money -= db
		else:
			receive(users, debts, user, money)
			debts[receiver].appendleft((user, db-money))
			money = 0
	# don't have any more debts
	users[receiver] += money

def send(users, debts, sender, receiver, money):
	current = users[sender]
	if current >= money: # if sender has enough money
		users[sender] -= money
		receive(users, debts, receiver, money)
	else:
		users[sender] = 0
		receive(users, debts, receiver, current)
		debts[sender].append((receiver, money-current))

def print_d(d: dict):
	for k,v in d.items():
		print(f"{k} --> {v}")

with open(filename) as f:
	counts, trans = f.read().split("\n\n")
	users = {}
	debts = {}
	for c in counts.splitlines():
		u, balance = c.split(" HAS ")
		users[u] = int(balance)
	for k in users.keys():
		debts[k] = deque()
	l = users.values()
	print(f"Initial total money: {sum(l)}")
	for t in trans.splitlines():
		s,d = t.split(" TO ")
		s = s[5:]
		d, m = d.split(" AMT ")
		send(users,debts, s, d, int(m))
	l = users.values()	
	print_d(debts)
	print_d(users)
	print(sum(sorted(l, reverse=True)[:3]))
	print(f"Final total money: {sum(l)}")	
	
