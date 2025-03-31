import sys
import numpy as np
filename = sys.argv[1]
dp = {}
def minpath(grid, pos, end):
    if pos in dp:
        return dp[pos]
    cx, cy = pos
    print(cx,cy)
    m = len(grid)
    n = len(grid[0])
    if cx not in range(m) or cy not in range(n):
        return float("inf")
    if pos == end:
        return grid[cx][cy]
    down = minpath(grid, (cx+1, cy), end)
    right = minpath(grid, (cx, cy+1), end)
    ans = grid[cx][cy] + min(down, right)
    dp[pos] = ans
    return ans

with open(filename) as f:
    grid = [[int(x) for x in y.split(" ")] for y in f.read().strip().splitlines()]
    start = (0,0)
    lx, ly = len(grid), len(grid[0])
    end = (lx-1,ly-1)
    print(minpath(grid, start, end))

    
    
    
