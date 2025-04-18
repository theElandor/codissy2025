import sys
filename = sys.argv[1]
def mem(s):
    ans = 0
    for c in s:
        if c.isdigit():
            ans += int(c)
        else:
            ans += ord(c)-64
    return ans
with open(filename) as f:
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        n = len(l)
        to_keep = n // 10
        beg = l[:to_keep]
        end = l[::-1][:to_keep]
        numeric = n - (2*to_keep)
        s = beg + str(numeric) + end
        ans += mem(s)
    print(ans)
        
