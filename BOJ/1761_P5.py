from collections import defaultdict
import sys
import math

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
parent = [[] for _ in range(N)]
dist = defaultdict(lambda: 0)
depth = [-1] * N
for _ in range(N-1):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    dist[(a-1,b-1)] = w
    dist[(b-1,a-1)] = w

root = 0
max_depth = 1
depth[root] = 1

st = [root]
while st:
    node = st.pop()
    max_depth = max(max_depth, depth[node])
    for i in graph[node]:
        if depth[i] == -1:
            st.append(i)
            parent[i].append(node)
            depth[i] = depth[node] + 1
            dist[(root, i)] = dist[(root,node)] + dist[(node,i)]

table_max = math.ceil(math.log(max_depth, 2))

parent[root].append(root)
for k in range(1, table_max):
    for i in range(N):
        parent[i].append(parent[parent[i][k-1]][k-1])

def lca(a, b):
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
        for k in range(table_max-1 , -1, -1):
            if parent[a][k] != -1 and parent[a][k] != parent[b][k]:
                a = parent[a][k]
                b = parent[b][k]
        a = parent[a][0]
    return a


M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    _lca = lca(a, b)
    print(dist[(root, a)] + dist[(root, b)] - 2 * dist[(root, _lca)])