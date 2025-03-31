import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().splitlines()
    total = 0
    for el in data:
        boxes = set()
        for r in el.split(" "):
            lb, ub = [int(x) for x in r.split("-")]
            for b in range(lb, ub+1):
                boxes.add(b)
        total += len(boxes)
    print(total)
     
