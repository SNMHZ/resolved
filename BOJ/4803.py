import sys

cnt = 1
while True:
    N, M = map(int, sys.stdin.readline().split())

    if N == 0 and M == 0:
        break

    edges = [ list(map(lambda x: int(x)-1, sys.stdin.readline().split())) for _ in range(M) ]
    
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

    cycleset = set()
    for edge in edges:
        if find(edge[0]) == find(edge[1]):
            cycleset.add(find(edge[0]))
        else:
            union(edge[0], edge[1])
            
    res = len(set([find(i) for i in range(N)]) - set([ find(i) for i in cycleset ]))
    print("Case {}: ".format(cnt), end="")
    if res == 0:
        print("No trees.")
    elif res == 1:
        print("There is one tree.")
    else:
        print("A forest of {} trees.".format(res))

    cnt += 1
