import sys
filename = sys.argv[1]
def swap_(l:list, i1,i2):
	temp = l[i1]
	l[i1] = l[i2]
	l[i2] = temp

def find_block(l, x,y):
	o1 = abs(x-y)
	o2 = abs(len(l)-max(x,y))
	return (min(o1,o2))


# x->y->z->x
with open(filename) as f:
	grid = f.read().splitlines()
	print(grid)
with open(filename) as f:
	tracks, swaps, target = f.read().split("\n\n")
	tracks = tracks.splitlines()
	swaps = swaps.splitlines()
	l = []
	for swap in swaps:
		s,t = [int(x)-1 for x in swap.split("-")]
		l.append(s)
		l.append(t)
	print(l)
	for swap in swaps:
		x,y = [int(_)-1 for _ in swap.split("-")]
		size = find_block(tracks, x, y)
		for i in range(size):
			swap_(tracks, x+i, y+i)		
		print(f"{x},{y} -> {size}")
	print(tracks[int(target)-1])
