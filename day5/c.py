import sys
import math
filename = sys.argv[1]

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def find_closest(sx, sy, unseen):
    closest = None
    mind = float("inf")
    for x,y in unseen:
        d = dist(sx,sy,x,y)
        if d < mind:
            mind = d
            closest = (x,y)
        if d == mind:
            cx, cy = closest
            if x < cx:
                closest = (x,y)
    return mind, closest

with open(filename) as f:
    data = f.read().splitlines()
    coords = []
    for d in data:
        x,y = d.split(", ")
        x = int(x[1:])
        y = int(y[:-1])
        coords.append((x,y))
    s = 0
    current = (0,0)    
    while coords:        
        d, n = find_closest(*current, coords)
        s += d
        coords.remove(n)
        current = n 
    print(s)

        

    
