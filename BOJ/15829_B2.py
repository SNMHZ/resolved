import sys

N = int(sys.stdin.readline())
_str = sys.stdin.readline().strip()

M = 1234567891

a = 0
h = 1
for i in range(len(_str)):
    a += ((ord(_str[i])-ord('a')+1) * h) % M
    h = (h * 31) % M
    a %= M

print(a)