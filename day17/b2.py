import sys
from collections import deque
from copy import deepcopy
import graphviz
filename = sys.argv[1]
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

def dp(G, node, moves, path):
	if node in memo:
		return memo[node]
	if node == "S1_0":
		paths.append(path)
		return 1
	neigs = list(neighbors(G,node,moves))
	ways = 0
	for n in neigs:
		ways += dp(G, n, moves, path+f"-{n[::-1]}")
	memo[node] = ways
	return ways

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
		name = line.split(" : ")[0]
		entry, exit = line.split(" : ")[2].split(" TO ")
		entry = entry.strip().split(" ")[1]
		exit = exit.strip()
		if l == 0:
			endpoint = end
		# ------------------ build reversed DAG
		# create the line
		for i in range(start, end+1):
			node_name = f"{name}_{str(i)}"
			if node_name not in G:
				G[node_name] = []
				dot.node(node_name)
		for i in range(end, start, -1):
			G[f"{name}_{i}"].append(f"{name}_{i-1}")
			dot.edge(f"{name}_{i}", f"{name}_{i-1}")
		if l == 0: continue
		# create the cross connections
		# dot.edge(f"{name}_{start}", f"{entry}_{start}")
		# dot.edge(f"{name}_{start}", f"{entry}_{start}")
		G[f"{name}_{start}"].append(f"{entry}_{start}")		
		G[f"{exit}_{end}"].append(f"{name}_{end}")
#		print(G)
	print(G)
	ans = dp(G, f"S1_{endpoint}", moves, "6_1S")
	print(memo)
	print(ans)
#	dot.render("graph.gv")