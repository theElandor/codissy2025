import sys
filename = sys.argv[1]
X,Y,Z,A = (10,15,60,3)

def get_mult(fun):
	mults = []
	for block in fun.split("+"):
		mults.append(int(block[:-1]))
	return mults
with open(filename) as f:
	rules = f.read().splitlines()
	for r,rule in enumerate(rules):
		p1, p2 = rule.split(" | ")
		print(p1.split(" "))		
		_,_,fun,_,divisor,_,_,rem = p1.split(" ")
		debris = eval(p2[16:])
		divisor, rem = int(divisor), int(rem)
		print(debris)
		rocks = []
		for x in range(X):
			for y in range (Y):
				for z in range(Z):
					for a in [-1,0,1]:
						m1,m2,m3,m4 = get_mult(fun)
						res = (m1*x)+(m2*y)+(m3*z)+(m4*a)
						if res % divisor == rem:
							rocks.append((r,x,y,z,a))
	print(len(rocks))