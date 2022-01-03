import sys

N, M, K = map(int, sys.stdin.readline().split())
friends = list(map(int, sys.stdin.readline().split()))
graph = dict([[i, []] for i in range(N)])
for i in range(M):
    v, w = map(int, sys.stdin.readline().split())
    graph[v-1].append(w-1)
    graph[w-1].append(v-1)

parent = [ i for i in range(N) ]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(N):
    for j in graph[i]:
        union(i, j)

roots = set()
min_vals = [float('inf')] * N
for i in range(N):
    roots.add(find(i))
    if min_vals[find(i)] > friends[i]:
        min_vals[find(i)] = friends[i]

_sum = 0
for i in roots:
    _sum += min_vals[i]

print(_sum if _sum <= K else 'Oh no')