import sys

N, M = map(int, sys.stdin.readline().split())
games = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(M) ]

parent = [-1] * N

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

isCycle = False
for i in range(M):
    x, y = games[i]
    if find(x) != find(y):
        union(x, y)
    else:
        isCycle = True
        print(i+1)
        break

if not isCycle:
    print(0)