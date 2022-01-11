import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
_str = sorted(sys.stdin.readline().split())

def check(_str):
    vow, con = 0, 0
    for c in _str:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
        else:
            con += 1
    return True if vow >= 1 and con >= 2 else False


for item in combinations(_str, L):
    if check(item):
        print(*item, sep='')