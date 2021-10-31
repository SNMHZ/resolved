def func_R():
    pass

def func_D():
    pass

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()[:-2]
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline()[1:-2].split(',')))

    print(p, n, arr)