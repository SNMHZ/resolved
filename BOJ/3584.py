import sys
import math

T = int(sys.stdin.readline())
while T:
    T -= 1

    # input
    N = int(sys.stdin.readline())
    child = [[] for _ in range(N)]
    parent = [[] for _ in range(N)]
    depth = [-1] * N
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        child[a-1].append(b-1)
        parent[b-1].append(a-1)
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())

    # find root. fan-in이 없는 것
    root = 0
    for i in range(N):
        if not parent[i]:
            root = i
            break

    # dfs
    # root의 depth 1로 초기화, 노드들의 depth 연산
    # 연산 과정에서 max_depth 획득하도록 함
    # 방향성이 있는 그래프로, 방문 여부 확인할 필요 없음
    depth[root] = 1
    max_depth = 1

    st = [root]
    while st:
        node = st.pop()
        max_depth = max(max_depth, depth[node])
        for leaf in child[node]:
            st.append(leaf)
            depth[leaf] = depth[node] + 1
    
    # 이진으로 올라가는 범위(유지해야 하는 크기) 계산
    table_max = math.ceil(math.log(max_depth, 2))
    
    # root의 parent는 fan-in이 없으므로 자기 자신 하나 넣어줌
    # 자신의 2^i번째 부모는 -> 자신의 2^(i-1)번째 부모의 2^(i-1)번째 부모
    # 일종의 DP
    parent[root].append(root)
    for k in range(1, table_max):
        for i in range(N):
            parent[i].append(parent[parent[i][k-1]][k-1])

    # find lca
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
        for k in range(table_max-1, -1, -1):
            if parent[a][k] != parent[b][k]:
                a = parent[a][k]
                b = parent[b][k]
        a = parent[a][0]

    print(a+1)