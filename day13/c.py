import sys
from collections import deque
from heapq import heappop, heappush
filename = sys.argv[1]
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
    dist = {}
    Q = []
    start = "STT"
    heappush(Q, (0,start))
    while Q:
        distance, current = heappop(Q)
        if current not in dist:
            dist[current] = distance
        if current not in G:
            continue
        for cost, dest in G[current]:
            if dest not in dist:
                heappush(Q, (distance+cost, dest))                
    print(dist)
    d = sorted([val for key, val in dist.items()], reverse=True)
    print(d[0]*d[1]*d[2])
