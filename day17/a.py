memo = {}
def dp(case, moves) -> int:
	if case in memo:
		return memo[case]
	if case < 0:
		return 0
	if case == 0:
		return 1
	final = 0
	for m in moves:
		final += dp(case-m, moves)
	memo[case] = final
	return final

filename = sys.argv[1]
with open(filename) as f:
	data = f.read().splitlines()
	initial = data[0]
	moves = list(map(int, data[-1].split(" : ")[1].split(", ")))
	start = int(initial.split("->")[0].split(" : ")[1].strip())
	end = int(initial.split("->")[1].split(" : ")[0].strip())
	print(dp(end, moves))

