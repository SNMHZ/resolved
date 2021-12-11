import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted([ list(map(int, sys.stdin.readline().split())) for _ in range(M) ], key=lambda x: x[2])

parent = [ -1 for _ in range(N+1) ]

# weighted quick union
def find(x):
    if parent[x] < 0:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

_sum = 0
weight_list = []
for i in range(M):
    x, y, w = data[i]
    if find(x) != find(y):
        union(x, y)
        _sum += w
        weight_list.append(w)

print(_sum - weight_list[-1])