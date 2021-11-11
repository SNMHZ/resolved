# python3은 타임아웃, pypy3은 통과
# 더 빠르게 되나..?

import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().split())
_map = [ list( map(int, sys.stdin.readline().split())) for _ in range(N)]
zeros = []
viruses = []
for i in range(N):
    for j in range(M):
        if _map[i][j] == 0:
            zeros.append( (i, j) )
        elif _map[i][j] == 2:
            viruses.append( (i, j) )

def expand(x, y, _map, q: deque):
    for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and _map[nx][ny]==0:
            q.append((nx, ny))

def spread_virus(_map):
    q = deque()
    q.extend(viruses)
    while(q):
        x, y = q.popleft()
        _map[x][y] = 2
        expand(x, y, _map, q)

    return _map

def count_safezone(_map):
    count = 0
    for m in _map:
        for elem in m:
            if elem == 0:
                count+=1
    return count

max_safe = 0
for w0, w1, w2 in combinations(zeros, 3):
    space = copy.deepcopy(_map)
    space[w0[0]][w0[1]] = 1
    space[w1[0]][w1[1]] = 1
    space[w2[0]][w2[1]] = 1

    max_safe = max(count_safezone(spread_virus(space)), max_safe)

print(max_safe)