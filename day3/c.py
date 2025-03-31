import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
    total = 0
    poss = []
    for p1, p2 in zip(data[:-1], data[1:]):
        boxes = set()
        for z in [p1.split(" "), p2.split(" ")]:
            for r in z:
                lb, ub = [int(x) for x in r.split("-")]
                for item in range(lb,ub+1):
                    boxes.add(item)
                poss.append(len(boxes))
    print(max(poss))
