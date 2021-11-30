import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

# Prim's Algorithm
data = [[] for _ in range(V+1)]

for _ in range(E):
    x, y, w = map(int, sys.stdin.readline().split())
    data[x].append((y, w))
    data[y].append((x, w))

def get_MST_Cost_ByPrim(start=1):
    pq = []
    mst_cost = 0
    visited = [False] * (V+1)
    visited[start] = True
    for y, w in data[start]:
        heapq.heappush(pq, (w, y))
    while pq:
        w, y = heapq.heappop(pq)
        if not visited[y]:
            mst_cost += w
            visited[y] = True
            for z, w in data[y]:
                if not visited[z]:
                    heapq.heappush(pq, (w, z))
    return mst_cost

print(get_MST_Cost_ByPrim())

# Krukal's Algorithm
# data = sorted([ list(map(int, sys.stdin.readline().split())) for _ in range(E) ], key=lambda x: x[2])

# parent = [ -1 for _ in range(V+1) ]

# # weighted quick union
# def find(x):
#     if parent[x] < 0:
#         return x
#     else:
#         parent[x] = find(parent[x])
#         return parent[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x == y:
#         return
#     if parent[x] < parent[y]:
#         parent[x] += parent[y]
#         parent[y] = x
#     else:
#         parent[y] += parent[x]
#         parent[x] = y

# _sum = 0
# for i in range(E):
#     x, y, w = data[i]
#     if find(x) != find(y):
#         union(x, y)
#         _sum += w

# print(_sum)