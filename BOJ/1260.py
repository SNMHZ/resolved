import sys

N, M, V = map(int, sys.stdin.readline().split())
edges = [ [] for _ in range(N) ]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

visited = [ False ] * N


def dfs(v):
    print(v+1, end=' ')
    visited[v] = True
    for i in sorted(edges[v]):
        if not visited[i]:
            dfs(i)

dfs(V-1)
print()

# visited = [ False ] * N
# st = [V-1]
# while st:
#     v = st.pop()
#     if not visited[v]:
#         visited[v] = True
#         for i in sorted(edges[v], reverse=True):
#             if not visited[i]:
#                 st.append(i)
# print()

visited = [ False ] * N
def bfs(v):
    q = [ v ]
    visited[v] = True
    while q:
        v = q.pop(0)
        print(v+1, end=' ')
        for i in sorted(edges[v]):
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(V-1)