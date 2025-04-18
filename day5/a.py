import sys
filename = sys.argv[1]

def dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)
    
with open(filename) as f:
    data = f.read().splitlines()
    poss = []
    for d in data:
        x,y = d.split(", ")
        x = int(x[1:])
        y = int(y[:-1])
        print(dist(0,0,x,y))
        poss.append(dist(0,0,x,y))
    print(max(poss) - min(poss))
    
        
