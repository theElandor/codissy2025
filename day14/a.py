import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
    its = {}
    for line in data:
        ID = line.split(" | ")[0].split(" ")[1]
        qual, cost, mats = line.split(" | ")[1].split(", ")
        its[ID] = (int(qual.split(" : ")[1]),int(cost.split(" : ")[1]),int(mats.split(" : ")[1]) )
    ordered = sorted(its.values(), key=lambda x:(x[0],x[1]), reverse=True)
    print(sum([o[2] for o in ordered[:5]]))
        
