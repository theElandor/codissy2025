import sys
from collections import deque
from copy import deepcopy
import graphviz
filename = sys.argv[1]
target = int(sys.argv[2])
memo = {}
paths = []
def neighbors(G, node, moves) -> list:
	# given a node, returns all possible neighbors
	# (allowed magnitudes)
	Q = deque()
	solutions = set()
	for m in moves:
		Q.append((node, m))
	while Q:
		current, m = Q.popleft()
		if m == 0:
			solutions.add(current)
		else:
			for dest in G[current]:
				Q.append((dest, m-1))
	return solutions

def dp(G, node, moves, endpoint):
	if node in memo:
		return memo[node]
	if node == endpoint:
		return 1
	neigs = list(neighbors(G,node,moves))
	ways = 0
	for n in neigs:
		ways += dp(G, n, moves, endpoint)
	memo[node] = ways
	return ways

def safer(node, target, G, moves, path, endpoint):
	current = node
	while current != endpoint:
		for n in sorted(neighbors(G, current, moves)):
			if target > memo[n]:
				target -= memo[n]
			else:
				path.append(n)
				current = n
				break



with open(filename) as f:
	raw = f.read()
	dot = graphviz.Digraph()
	data = raw.splitlines()
	initial = data[0]
	moves = list(map(int, data[-1].split(" : ")[1].split(", ")))
	start = int(initial.split("->")[0].split(" : ")[1].strip())
	end = int(initial.split("->")[1].split(" : ")[0].strip())
	sts = raw.split("\n\n")[0].splitlines()
	G = {}
	for l,line in enumerate(sts):
		start = int(line.split("->")[0].split(" : ")[1].strip())
		end = int(line.split("->")[1].split(" : ")[0].strip())
		name = int(line.split(" : ")[0][1:])
		if l != 0:
			entry, exit = line.split(" : ")[2].split(" TO ")
			entry = int(entry.strip().split(" ")[1][1:])
			exit = int(exit.strip()[1:])
		if l == 0:
			endpoint = (name, end)
		# ------------------ build reversed DAG
		# create the line
		for i in range(start, end+1):
			if (name, i) not in G:
				G[(name, i)] = []
		for i in range(start,end):
			G[(name, i)].append((name, i+1))
		if l == 0: continue
		# create the cross connections
		G[(entry, start)].append((name, start))
		G[(name, end)].append((exit, end))
	print(G)
	print(f"Try to reach {endpoint}")
	ans = dp(G,(1,0), moves, endpoint)
	path = [(1,0)]
	memo[endpoint] = 1
	safer((1,0), target, G, moves, path, endpoint)
	print("-".join([f"S{x[0]}_{x[1]}" for x in path]))
