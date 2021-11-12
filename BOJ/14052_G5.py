# 바이러스 퍼트리면서 동시에 카운트
# + 퍼트려 보다가 max 이하로 가버리면 더 안퍼트리고 탐색 중지
# dfs하면 더 빠를듯? 콘솔에선 더 빠른데 백준은 쪼매 더 느려짐(사실 큰 차이는 없음)

import sys
from collections import deque
from itertools import combinations

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

BLANK_SPACE_SIZE = len(zeros) - 3

def spread_virus(_map, result):
    q = deque()
    q.extend(viruses)
    count = BLANK_SPACE_SIZE
    while(q):
        if count < result: break
        x, y = q.pop()
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not _map[nx][ny]:
                _map[nx][ny] = 2
                q.append((nx, ny))
                count -= 1
    return count

max_safe = 0
for w0, w1, w2 in combinations(zeros, 3):
    space = [d[:] for d in _map ]
    space[w0[0]][w0[1]] = 1
    space[w1[0]][w1[1]] = 1
    space[w2[0]][w2[1]] = 1

    max_safe = max(spread_virus(space, max_safe), max_safe)

print(max_safe)