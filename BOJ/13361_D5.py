import sys
sys.setrecursionlimit(250000)
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

parent = [i for i in range(N*2)]
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
    if parent[x] < parent[y]:
        parent[x] = y
    else:
        parent[y] = x

_sum = 0
val = []
val_idx = {}
_count = [0]*(N*2)
for i in range(N):
    x, y = data[i]
    if x not in val_idx:
        val_idx[x] = len(val)
        val.append(x)

    if y not in val_idx:
        val_idx[y] = len(val)
        val.append(y)

    union(val_idx[x], val_idx[y])

    _count[find(val_idx[x])] += 1
    _sum += x + y

group = [ [] for _ in range(len(val)) ]
roots = []
for i in range(len(val)):
    if find(i) == i:
        roots.append(i)
    else:
        _count[find(i)] += _count[i]
    group[find(i)].append(val[i])

for root in roots:
    _sum-=sum(sorted(group[root])[:_count[root]])

print(_sum)