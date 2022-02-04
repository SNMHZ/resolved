import sys
import math
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
child = [[] for _ in range(N)]
parent = [[] for _ in range(N)]
depth = [-1] * N
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    child[a-1].append(b-1)
    child[b-1].append(a-1)

root = 0
max_depth = 0
depth[root] = 0
# st = [root]
# depth[root] = 1
# 
# while st:
#     node = st.pop()
#     max_depth = max(max_depth, depth[node])
#     for i in child[node]:
#         if depth[i] == -1:
#             st.append(i)
#             parent[i].append(node)
#             depth[i] = depth[node] + 1

def dfs(node):
    global max_depth
    max_depth = max(max_depth, depth[node])
    for i in child[node]:
        if depth[i] == -1:
            parent[i].append(node)
            depth[i] = depth[node] + 1
            # print(node, parent)
            dfs(i)

dfs(0)
table_max = math.ceil(math.log(N, 2))

del child
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
    print(lca(a, b)+1)