import sys
filename = sys.argv[1]
def swap_(l:list, i1,i2):
	temp = l[i1]
	l[i1] = l[i2]
	l[i2] = temp
with open(filename) as f:
	tracks, swaps, target = f.read().split("\n\n")
	tracks = tracks.splitlines()
	swaps = swaps.splitlines()
	for swap in swaps:
		s,t = [int(x)-1 for x in swap.split("-")]
		swap_(tracks,s,t)
	print(tracks[int(target)-1])
    # here
