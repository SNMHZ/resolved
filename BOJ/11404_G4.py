import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = [[float('inf')]*N for _ in range(N)]

for i in range(N):
    edges[i][i] = 0

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    if edges[a-1][b-1] > w:
        edges[a-1][b-1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if edges[i][k] + edges[k][j] < edges[i][j]:
                edges[i][j] = edges[i][k] + edges[k][j]

for i in range(N):
    for j in range(N):
        if edges[i][j] == float('inf'):
            edges[i][j] = 0

for i in range(N):
    print(*edges[i])