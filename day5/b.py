import sys
import math
filename = sys.argv[1]
def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
    
with open(filename) as f:
    data = f.read().splitlines()
    closest = None
    mind = float("inf")
    for d in data:
        x,y = d.split(", ")
        x = int(x[1:])
        y = int(y[:-1])
        d = dist(0,0,x,y)
        if d < mind:
            mind = d
            closest = (x,y)
        if d == mind:
            cx, cy = closest
            if x < cx:
                closest = (x,y)
    print(closest)
    cx, cy = closest
    ans = []
    for d in data:        
        x,y = d.split(", ")
        x = int(x[1:])
        y = int(y[:-1])
        if (x,y) == closest:
            continue
        d = dist(cx,cy,x,y)
        ans.append(d)
    print(min(ans))
            
            
                
        
        

    
