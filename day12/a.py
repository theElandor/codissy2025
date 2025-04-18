import sys
filename = sys.argv[1]
import numpy as np
def correct_values(grid):
    while True:
        ops = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    grid[i][j] = 1073741824 - abs(grid[i][j])
                    ops += 1
                elif grid[i][j] >= 1073741824:
                    grid[i][j] = grid[i][j] - 1073741824
                    ops += 1
        if ops == 0:
            break
        
def row_op(grid, index, op, n):
    for j in range(len(grid[0])):
        grid[index][j] = eval(f"grid[index][j] {op} {n}")
    correct_values(grid)
    
def col_op(grid, index, op, n):
    for i in range(len(grid)):
        grid[i][index] = eval(f"grid[i][index] {op} {n}")
    correct_values(grid)
d = {"MULTIPLY": "*",
     "ADD": "+",
     "SUB": "-",
     }

def shift_row(grid, index, n):
    cols = len(grid[0])
    for t in range(n):
        temp = grid[index][cols-1]
        for i in range(cols-1, 0, -1):
            grid[index][i] = grid[index][i-1]
        grid[index][0] = temp

def shift_col(grid, index, n):
    rows = len(grid)
    for t in range(n):
        temp = grid[rows-1][index]
        for i in range(rows-1, 0,-1):
            grid[i][index] = grid[i-1][index]
        grid[0][index] = temp

def print_grid(grid):
    for row in grid:
        print(" ".join([str(x) for x in row]))

def perform(op):
    command = op.split(" ")[0]
    if command in "MULTIPLY SUB ADD":
        n = int(op.split(" ")[1])
        next = op.split(" ")[2]
        if next == "ALL":
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    grid[i][j] = eval(f"grid[i][j] {d[command]} n")
            correct_values(grid)
        else:
            target = op.split(" ")[2]
            index = int(op.split(" ")[3])-1
            if target == "ROW":
                row_op(grid, index, d[command], n)
            else:
                col_op(grid, index, d[command], n)
    elif command == "SHIFT":
        # print("shifting")
        target = op.split(" ")[1]
        index = int(op.split(" ")[2])-1
        n = int(op.split(" ")[4])
        if target == "ROW":
            shift_row(grid, index, n)
        else:
            shift_col(grid, index, n)                    
        
with open(filename) as f:
    grid, ops, actions = f.read().strip().split("\n\n")
    grid = [[int(x) for x in y.split(" ")] for y in grid.splitlines()]
    ops = ops.splitlines()
    a = 0
    actions = actions.splitlines()
    while True:
        action = actions[a]
        if action == "TAKE":
            try:
                current = ops[0]
            except:
                break
            ops.pop(0)
        elif action == "CYCLE":
            ops.append(current)
        elif action == "ACT":
            perform(current)
        a = (a+1)%len(actions)
        if a == 0:
            print("-------------")
            print_grid(grid)
            print(ops)

            
    arr = np.array(grid)
    rows = np.sum(grid, axis=0)
    cols = np.sum(grid, axis=1)
    print(max(max(rows),max(cols)))
