import sys
filename = sys.argv[1]
# weight -> we alredy have
memo = {}
def best_weight(all_items, weight, index, value, taken="", mats_fn=0):
    if (weight, index, value) in memo:
        return memo[(weight, index, value)]
    if weight > 300:
        return -float("inf"), "nope", float("inf")
    if index == len(all_items) or weight == 300:
        return value, taken, mats_fn
    ID, qual,cost,mats = all_items[index]
    poss1, path1, m1= best_weight(all_items, weight+cost, index+1, value+qual, taken+f" {ID}",mats_fn+mats)
    poss2, path2, m2= best_weight(all_items, weight, index+1, value, taken, mats_fn)
    if poss1 > poss2:
        memo[(weight, index, value)] = (poss1, path1, m1)
        return poss1, path1, m1
    elif poss1 == poss2:
        if m1 > m2:
            memo[(weight, index, value)] = (poss2, path2, m2)
            return poss2, path2, m2
        else:
            memo[(weight, index, value)] = (poss1, path1, m1)
            return poss1, path1, m1
    else:
        memo[(weight, index, value)] = (poss2, path2, m2)
        return poss2, path2, m2

    
with open(filename) as f:
    data = f.read().splitlines()
    its = {}
    for line in data:
        ID = line.split(" | ")[0].split(" ")[1]
        qual, cost, mats = line.split(" | ")[1].split(", ")
        its[ID] = (int(qual.split(" : ")[1]),int(cost.split(" : ")[1]),int(mats.split(" : ")[1]))
    all_items = [[key] + list(val) for key, val in its.items()]
    val, taken, mats = best_weight(all_items, 0, 0, 0)
    tot_weight = 0
    for ID in taken.strip().split(" "):        
        tot_weight += its[ID][1]
    print(tot_weight)
    print(mats, val)
    print(mats*val)
    
    
        
