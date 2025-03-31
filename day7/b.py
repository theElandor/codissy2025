import sys
filename = sys.argv[1]
def swap_(l:list, i1,i2):
	temp = l[i1]
	l[i1] = l[i2]
	l[i2] = temp
# x->y->z->x
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
	for i in range(0,len(l)-1,2):
		x,y = l[i], l[i+1]
		z = l[(i+2)%len(l)]
		print(x,y,z)
		temp = tracks[x]
		tracks[x] = tracks[z]
		tracks[z] = tracks[y]
		tracks[y] = temp
		print(x+1, y+1, z+1)
	print(tracks[int(target)-1])
