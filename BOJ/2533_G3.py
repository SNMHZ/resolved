import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
graph = {}
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)


dp = [ [1, 0] for _ in range(N+1) ]
visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
            dp[v][1] += dp[u][0]
            dp[v][0] += min(dp[u])
    del graph[v]

dfs(1)
print(min(dp[1]))