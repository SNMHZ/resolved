# ref: https://blog.naver.com/kks227/220804885235
# 아직 이해 못함

import sys
from collections import deque

N = int(sys.stdin.readline())
def ctoi(c):
    if c <= 'Z':
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

capa = [ [0] * 52 for _ in range(52) ]
conn = [ [] for _ in range(52) ]
for _ in range(N):
    a, b, w = sys.stdin.readline().split()
    a, b, w = ctoi(a), ctoi(b), int(w)
    capa[a][b] += w
    capa[b][a] += w
    conn[a].append(b)
    conn[b].append(a)

flow = [[0] * 52 for _ in range(52)]



total = 0
while True:
    prev = [ -1 for _ in range(52)]
    q = deque([ctoi('A')])
    while q and prev[ctoi('Z')] == -1:
        cur = q.popleft()
        for nxt in conn[cur]:
            if capa[cur][nxt] > flow[cur][nxt] and prev[nxt] == -1:
                prev[nxt] = cur
                q.append(nxt)
                if nxt == ctoi('Z'):
                    break
    if prev[ctoi('Z')] == -1:
        break
    cur_flow = float('inf')
    cur = ctoi('Z')
    while True:
        cur_flow = min(cur_flow, capa[prev[cur]][cur] - flow[prev[cur]][cur])
        cur = prev[cur]
        if cur == ctoi('A'):
            break
    cur = ctoi('Z')
    while True:
        flow[prev[cur]][cur] += cur_flow
        flow[cur][prev[cur]] -= cur_flow
        cur = prev[cur]
        if cur == ctoi('A'):
            break
    total += cur_flow

print(total)