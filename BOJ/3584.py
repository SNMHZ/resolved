import sys

T = int(sys.stdin.readline())
while T:
    T -= 1
    N = int(sys.stdin.readline())
    child = [[] for _ in range(N)]
    parent = [[] for _ in range(N)]
    depth = [0] * N
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        child[a-1].append(b-1)
        parent[b-1].append(a-1)
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    root = 0
    for i in range(N):
        if not parent[i]:
            root = i
            break
    
    st = [(root, 0)]
    max_depth = 0
    while st:
        node, d = st.pop()
        depth[node] = d
        max_depth = max(max_depth, d)
        for i in child[node]:
            st.append((i, d+1))
    del child
    parent[root].append(root)
    for k in range(1, max_depth):
        for i in range(N):
            parent[i].append(parent[parent[i][k-1]][k-1])

    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    k=0
    while diff:
        if diff % 2:
            a = parent[a][k]
        diff //= 2
        k += 1
    if a != b:
        for k in range(max_depth):
            if parent[a][k] != parent[b][k]:
                a = parent[a][k]
                b = parent[b][k]
        a = parent[a][0]
    
    print(a+1)