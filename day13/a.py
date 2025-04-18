import sys
from collections import deque
from heapq import heappop, heappush
sys.setrecursionlimit(1000000000)
filename = sys.argv[1]
visited = set()
poss = []
def dfs(G, start, current, pathlen, path):
    if current not in G: return    
    for d,v in G[current]:
        if v == start:
            poss.append((pathlen+d, path))
        elif v not in visited:
            visited.add(v)
            dfs(G, start, v, pathlen+d, path + f" {v}")
            visited.remove(v)

with open(filename) as f:
    data = f.read().splitlines()
    G = {}
    for line in data:
        source, dest = line.split(" -> ")
        dest, cost = dest.split(" | ")
        cost = int(cost)
        if source not in G:
            G[source] = [(cost, dest)]
        else:
            G[source].append((cost,dest))
    for start in G.keys():
        if start == "STT": continue
        dfs(G, start, start, 0, start)
        visited.clear()
    print(max(poss, key=lambda x:x[0]))
    
            
        
    
