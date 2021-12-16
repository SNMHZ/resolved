import sys

N, M = map(int, sys.stdin.readline().split())
max_edges = [[0]*N for _ in range(N)]
dist = [[float('inf')]*N for _ in range(N)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    # longest edge length
    if max_edges[a-1][b-1] < w:
        max_edges[a-1][b-1] = w
        max_edges[b-1][a-1] = w
    
    # Floyd-Warshall shortest path length
    if dist[a-1][b-1] > w:
        dist[a-1][b-1] = w
        dist[b-1][a-1] = w

for i in range(N):
    dist[i][i] = 0

# Floyd-Warshall
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = float('inf')
for start in range(N):
    res_burn_time = 0

    for from_ in range(N):
        for to_ in range(N):
            if max_edges[from_][to_] != 0:
                node_burn_time = (max_edges[from_][to_] - (dist[start][to_] - dist[start][from_]))/2 + dist[start][to_]
                res_burn_time = max(res_burn_time, node_burn_time)

    ans = min(ans, res_burn_time)

print(ans)