import sys
sols = set()
memos = {}
# Backtracking solution, works for small input, 
# for bigger input we need dynamic programming.

# start, end, entry, exit
def search(cc, cs, stairs, conns, steps) -> list:
	if (cc,cs,steps) in memos:
		return memos[(cc,cs,steps)]
	# returns the list of possible (case, stair)
	# if we are in case cc and stair cs and try moves
	if cc > stairs[cs][1]:
		return []
	if cc < stairs[cs][0]:
		return []
	if steps == 0:
		return [(cc, cs)]
	# go straight
	possibles = []
	forward = search(cc+1, cs, stairs, conns, steps-1)
	if forward:
		for el in forward:
			possibles.append(el)
	if (cs, cc) in conns:
		ns, nc = conns[(cs,cc)]
		turn = search(nc, ns, stairs, conns, steps-1)
		for sol in turn:
			possibles.append(sol)
	memos[(cc,cs,steps)] = possibles
	return possibles

def dump(paths):
	with open("test.txt", "w") as f:
		for path in paths:
			f.write(path+"\n")


def backtrack(cc, cs, visited, stairs, conns, moves, path):
	if cs == "S1" and cc == stairs["S1"][1]:
		sols.add(path)
	for move in moves: # try every possible move
		poss_next = search(cc, cs, stairs, conns, move) # check where i end up 
		for nc, ns in poss_next: # try to go there if not visited			
			if (nc,ns) not in visited:
				visited.add((nc,ns))
				backtrack(nc, ns, visited, stairs, conns, moves, path+f"-{ns}_{nc}")
				visited.remove((nc,ns)) # backtrack
	

filename = sys.argv[1]
with open(filename) as f:
	raw = f.read()
	data = raw.splitlines()
	initial = data[0]
	moves = list(map(int, data[-1].split(" : ")[1].split(", ")))
	start = int(initial.split("->")[0].split(" : ")[1].strip())
	end = int(initial.split("->")[1].split(" : ")[0].strip())
	sts = raw.split("\n\n")[0].splitlines()
	stairs = {} # name -> start, end
	conns = {} # name -> out_edges	
	for i, line in enumerate(sts):
		start = int(line.split("->")[0].split(" : ")[1].strip())
		end = int(line.split("->")[1].split(" : ")[0].strip())
		name = line.split(" : ")[0]
		entry, exit = line.split(" : ")[2].split(" TO ")
		entry = entry.strip().split(" ")[1]
		exit = exit.strip()
		stairs[name] = (start, end, entry, exit)
		if entry == "START" or end == "END": continue
		# {entry}{start} -> {name}{start}
		# {name}{end} -> {exit}{end}
		conns[(entry, start)] = (name, start)
		conns[(name, end)] = (exit, end)
	for k, v in conns.items():
		print(k,v)
	print("----------")
	backtrack(0, "S1", set(), stairs, conns, moves, "S1_0")
	print(len(sols))
	dump(sols)