import sys
from copy import deepcopy
from collections import deque
filename = sys.argv[1]
#X,Y,Z,A = (3,3,5,3)
max_t = 300
X,Y,Z,A = (10,15,60,3)
start = (0,0,0,0,0,0) #time, x, y, z, a, hits
#target = (2,2,4,0)
target = (9, 14, 59, 0)
directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1), (0,0,0)]
def get_mult(fun):
    mults = []
    for block in fun.split("+"):
        mults.append(int(block[:-1]))
    return mults

def get_rocks_at(t, rocks, d) -> set:
    new = {}
    for position, rules in rocks.items():
        x,y,z,a = position
        for r in rules:
            dx, dy, dz, da = d[r]
            nx,ny,nz,na = warp((x+(dx*t),y+(dy*t),z+(dz*t),a+(da*t)))
            if (nx,ny,nz,na) not in new:
                new[(nx,ny,nz,na)] = []         
            new[((nx,ny,nz,na))].append(r)
    return new

def warp(pos):
    x,y,z,a = pos
    nx = x % X
    ny = y % Y
    nz = z % Z
    na = a
    while na not in (-1,0,1):
        if na > 1: na -= A
        elif na < -1: na += A
    return (nx,ny,nz,na)


with open(filename) as f:
    rules = f.read().splitlines()
    d = {}
    rocks = {}
    for r,rule in enumerate(rules):
        p1, p2 = rule.split(" | ")
        print(p1.split(" "))        
        _,_,fun,_,divisor,_,_,rem = p1.split(" ")
        vel = eval(p2[16:])
        divisor, rem = int(divisor), int(rem)
        print(vel)
        d[r] = vel
        for x in range(X):
            for y in range (Y):
                for z in range(Z):
                    for a in [-1,0,1]:
                        m1,m2,m3,m4 = get_mult(fun)
                        res = (m1*x)+(m2*y)+(m3*z)+(m4*a)
                        if res % divisor == rem:
                            if (x,y,z,a) not in rocks:
                                rocks[(x,y,z,a)] = []
                            rocks[(x,y,z,a)].append(r)
    maps = {0:rocks}
    for t in range(1,max_t):
        maps[t] = get_rocks_at(t, rocks, d)
        print(f"{t}/{max_t} maps computed -> {len(maps[t])}")
    Q = deque()
    Q.append(start)
    visited = set()
    while Q:
        time, x, y, z, a, hits = Q.popleft()
        # if hits > 3:
        #   continue
        # if (x,y,z,a) == (0,0,0,0) or (x,y,z,a) not in maps[time]: 
        #   new_hits = 0
        # else:
        #   new_hits = len(maps[time][(x,y,z,a)])
        if (x,y,z,a) == target:
            print(f"reached {target} in {time} time units")
            break
        for dx, dy, dz in directions:
            da = 0
            if x+dx not in range(X) or y+dy not in range(Y) or z+dz not in range(Z) or a+da not in [-1,0,1]:
                continue
            dhits = 0 if (x+dx, y+dy, z+dz, a+da) == (0,0,0,0) or (x+dx,y+dy,z+dz,a+da) not in maps[time+1] else len(maps[time+1][(x+dx,y+dy, z+dz, a+da)])
            if hits + dhits > 3: continue
            if (time+1, x+dx,y+dy,z+dz,a+da, hits+dhits) not in visited:
                Q.append((time+1, x+dx,y+dy,z+dz,a+da, hits+dhits))
                visited.add((time+1, x+dx,y+dy,z+dz,a+da, hits+dhits))
