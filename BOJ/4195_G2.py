import sys

TC = int(sys.stdin.readline().strip())

def find(x, parent: list):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent: list, rank: list):
    x = find(x, parent)
    y = find(y, parent)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    rank[x] += rank[y]
    rank[y] = rank[x]

while TC:
    TC -= 1
    N = int(sys.stdin.readline().strip())

    swc = {}
    graph = {}
    parent = []
    rank = []
    for _ in range(N):
        A, B = sys.stdin.readline().split()
        if A not in swc:
            swc[A] = len(swc)
            graph[swc[A]] = []
            parent.append(swc[A])
            rank.append(1)
        if B not in swc:
            swc[B] = len(swc)
            graph[swc[B]] = []
            parent.append(swc[B])
            rank.append(1)
        graph[swc[A]].append(swc[B])
        graph[swc[B]].append(swc[A])
        union(swc[A], swc[B], parent, rank)
        print(rank[find(swc[A], parent)])
