import sys
filename = sys.argv[1]
def fun(n):
    return (((n ** 3)*79)+813)
with open(filename) as f:
    data = sorted([int(x) for x in f.read().splitlines()])
    poss = []
    for x in data:
        if fun(x) <= 15000000000000:
            poss.append(x)
    print(max(poss))
    
        
