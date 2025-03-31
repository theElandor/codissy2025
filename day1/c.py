import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
    print(data)
    signs = list(data[-1])[::-1]
    s = int(data[0])
    print(len(signs))
    numbers = [f"{data[i]}{data[i+1]}" for i in range(2, len(data)-2, 2)]
    print(numbers)
    s = int(f"{data[0]}{data[1]}")
    for i,n in enumerate(map(int, numbers)):
        s += eval(f"{signs[i]}{n}")
    print(s)
    
        
    # for i,x in enumerate(data[1:-1]):
    #     s += eval(f"{signs[i]}{x}")
    # print(s)
    

    
    
