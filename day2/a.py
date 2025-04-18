import sys
filename = sys.argv[1]
def fun(n):
    return (((n ** 3)*79)+813)
with open(filename) as f:
    data = sorted([int(x) for x in f.read().splitlines()])
    s = 0
    for x in data:
        if x % 2 == 0:
            s += x
    print(fun(s))
    
        
