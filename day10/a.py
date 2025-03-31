import sys
import numpy as np
filename = sys.argv[1]

with open(filename) as f:
    grid = [[int(x) for x in y.split(" ")] for y in f.read().strip().splitlines()]
    g = np.array(grid)
    print(g.shape)
    rows = np.sum(grid, axis=0)
    cols = np.sum(grid, axis=1)
    print(min(rows))
    print(min(cols))
