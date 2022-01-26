#벨만-포드
import sys

N, M = map(int, sys.stdin.readline().split())
edges = [ [] for _ in range(N) ]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges[A-1].append((B-1, C))

dist = [float('inf')] * N
dist[0] = 0
isMinusCycle = False

for _ in range(N-1):
    for i in range(N):
        for nxt, d in edges[i]:
            if dist[i] != float('inf') and dist[i] + d < dist[nxt]:
                dist[nxt] = dist[i] + d


for i in range(N):
        for nxt, d in edges[i]:
            if dist[i] != float('inf') and dist[i] + d < dist[nxt]:
                dist[nxt] = dist[i] + d
                isMinusCycle = True

if isMinusCycle:
    print(-1)
else:
    for i in range(1, N):
        print(dist[i] if dist[i] != float('inf') else -1)
