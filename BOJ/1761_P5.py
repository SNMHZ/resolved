import sys
sys.setrecursionlimit(10000)
N = int(sys.stdin.readline())
edges = [ list(map(int, sys.stdin.readline().split())) for _ in range(N-1) ]
M = int(sys.stdin.readline())
quarry = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]

parent = [-1]*N
def find(x):
    if parent[x] < x:
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

