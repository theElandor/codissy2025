import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
    print(data)
    signs = list(data[-1])[::-1]
    s = int(data[0])
    print(len(signs))
    for i,x in enumerate(data[1:-1]):
        s += eval(f"{signs[i]}{x}")
    print(s)
    

    
    
