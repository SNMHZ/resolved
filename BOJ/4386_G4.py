import sys
import heapq

N = int(sys.stdin.readline())
stars = [ tuple(map(float, sys.stdin.readline().split())) for _ in range(N)]

def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        graph[i].append((dist(stars[i], stars[j]), j))
        graph[j].append((dist(stars[j], stars[i]), i))

def get_MST_Cost_ByPrim(data, V, start=1):
    pq = []
    mst_cost = 0
    visited = [False] * (V+1)
    visited[start] = True
    for w, y in data[start]:
        heapq.heappush(pq, (w, y))
    while pq:
        w, y = heapq.heappop(pq)
        if not visited[y]:
            mst_cost += w
            visited[y] = True
            for w, z in data[y]:
                if not visited[z]:
                    heapq.heappush(pq, (w, z))
    return mst_cost

print(get_MST_Cost_ByPrim(graph, N, start=0))