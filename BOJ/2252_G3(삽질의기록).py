# 그래프가 몇개인지 세고 각 노드가 몇번 그래프에 속하는지와 깊이 마킹(BFS)
# 핵심 아이디어는 처음 탐색을 시작한 노드의 깊이를 0으로 하고, 부모는 그냥 음수 깊이를 해서 갱신하는 시간을 줄여보려 했다.

# 각 그래프의 말단(가장 깊은) 노드 중 하나 획득
# 같은 그래프 내에도 말단 깊이의 다른 노드가 있을 수 있으므로, 부모 노드로 이동 후 자식 노드 모두 리스트에 추가
# 부모 노드 기준으로 부모 노드 BFS로 탐색하며 리스트에 추가
# 모든 그래프에 대해 같은 행위 수행

# 틀림
# 임의의 말단의 부모들이 모든 말단을 알 리가 없다..!
# 결국 위상 정렬 공부해서 해결...
# 그래프 별 위상 정렬 정도로 활용할 수 있을 듯..?
# 삽질의 기록으로 남겨둬야지...

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
parent = [ [] for _ in range(N+1) ]
child = [ [] for _ in range(N+1) ]
for i in range(M):
    p, c = map(int, sys.stdin.readline().split())
    parent[c].append(p)
    child[p].append(c)

visited = [(-1, -1)] * (N+1)
graph_num = 0

for i in range(1, N+1):
    if visited[i][0] == -1:
        graph_num += 1
        q = deque([(i, 0)])
        while q:
            node, depth = q.popleft()
            visited[node] = (graph_num, depth)
            for child_node in child[node]:
                if visited[child_node][0] == -1:
                    q.append((child_node, depth+1))
            for parent_node in parent[node]:
                if visited[parent_node][0] == -1:
                    q.append((parent_node, depth-1))
graph_info = [(i, -1) for i in range(graph_num+1)] # graph_num (index, depth)
for i in range(1, N+1):
    g, d = visited[i]
    if graph_info[g][1] < d:
        graph_info[g] = (i, d)

for i in range(1, graph_num+1):
    idx, depth = graph_info[i]
    if not parent[idx]:
        print(idx, end=' ')
        continue
    arr = []
    for p in parent[idx]:
        for c in child[p]:
            if c not in arr:
                arr.append(c)
    
    q = deque(parent[idx])
    while q:
        node = q.popleft()
        arr.append(node)

        for p in parent[node]:
            q.append(p)
    for k in arr[::-1]:
        print(k, end=' ')