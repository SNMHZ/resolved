import sys

_str = sys.stdin.readline().rstrip()

res = 0

idx = 0
increasing = True
for i in range(len(_str)):
    if _str[i] == '+' or _str[i] == '-':
        cur = int(_str[idx:i])
        idx = i+1
        
    
        if increasing:
            res += cur
        else:
            res -= cur

        if not increasing or _str[i] == '-':
            increasing = False

cur = int(_str[idx:])

if increasing:
    res += cur
else:
    res -= cur

print(res)