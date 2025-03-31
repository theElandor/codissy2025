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

def compress(s):
    final = ""
    run = 1
    for i in range(len(s)):
        current = s[i]
        if i == len(s)-1:
            final += str(run)
            final += str(current)
            break
        next = s[i+1]
        if current == next:
            run += 1
        else:
            final += str(run)
            final += current
            run = 1
            current = next
    return final

with open(filename) as f:
    lines = f.read().splitlines()
    ans = 0
    for l in lines:
        f = compress(l)
        ans += mem(f)
    print(ans)
        
