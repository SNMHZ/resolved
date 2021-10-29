# 타임아웃과의 싸움
# PyPy3
# Python3는 타임아웃 ㅋ;

import sys
        
N, M, inventory = map(int, sys.stdin.readline().split())
ground = sum([list(map(int, sys.stdin.readline().split())) for _ in range(N)], [])
ans = float('inf')

level = 0
for lev in range(257):
    trim = 0
    fill = 0
    for g in ground:
        if g > lev:
            trim += g - lev
        else:
            fill += lev - g
    if inventory+trim < fill:
        continue
    timer = 2*trim + fill
    if timer <= ans:
        ans, level = timer, lev

print(ans, level)