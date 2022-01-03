# DFS로 해결해 보려고 했지만, 간선의 수가 너무 많아 시간초과
# 힙까지 만들어가면서 했는데 실패
# 결국 유니온 파인드 썼음.
import sys
import heapq

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

graph = {}
_sum = 0
for i in range(N):
    x, y = data[i]
    graph[x] = graph.get(x, []) + [i]
    graph[y] = graph.get(y, []) + [i]
    _sum += x + y

parent = [-1 for _ in range(N)]
# print(graph)
size = -1
_set = []
_count = []
for i in range(N):
    if parent[i] == -1:
        size += 1
        _set.append(set())
        _count.append(1)

        x, y = data[i]
        parent[i] = size

        st = []

        _set[size].add(x)
        #st += graph[x]
        st.extend(graph[x])
        if y not in _set[size]:
            _set[size].add(y)
            #st += graph[y]
            st.extend(graph[y])

        while st:
            node = st.pop()
            parent[node] = size
            cur_x, cur_y = data[node]
            if cur_x not in _set[size]:
                _set[size].add(cur_x)
                #st += graph[cur_x]
                st.extend(graph[cur_x])
            if cur_y not in _set[size]:
                _set[size].add(cur_y)
                #st += graph[cur_y]
                st.extend(graph[cur_y])
    else:
        _count[parent[i]] += 1

_heap = [ list(_set[i]) for i in range(size+1) ]
for i in range(size+1):
    heapq.heapify(_heap[i])

width_sum = 0
for i in range(size+1):
    for iter in range(_count[i]):
        width_sum += heapq.heappop(_heap[i])

print(_sum - width_sum)