import sys
import heapq

N, M, R = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
vertex = {}
for i in range(N):
    vertex[i] = []
for _ in range(R):
    a, b, cost = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    vertex[a].append((b, cost))
    vertex[b].append((a, cost))

dists = [[float('inf')] * N for _ in range(N)]

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dists[start][start] = 0
    while pq:
        cost, current = heapq.heappop(pq)
        
        if dists[start][current] < cost: # 이미 최소값이라면 무시
            continue

        for next, next_cost in vertex[current]:
            if dists[start][next] > dists[start][current] + next_cost:
                dists[start][next] = dists[start][current] + next_cost
                heapq.heappush(pq, (dists[start][next], next))

_pre_answers = []
for i in range(N):
    dijkstra(i)
    _sum = 0
    for j in range(N):
        if dists[i][j] <= M:
            _sum += t[j]
    _pre_answers.append(_sum)

print(max(_pre_answers))