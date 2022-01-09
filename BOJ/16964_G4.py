import sys

N = int(sys.stdin.readline())
edges = {}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
    edges[a].append(b)
    edges[b].append(a)

travels = list(map(int, sys.stdin.readline().split()))
_order = [0]*(N+1)
for i in range(len(travels)):
    _order[travels[i]] = i


visited = [-1] * (N+1)

st = []
st.append([travels[0], 0])
visited[travels[0]] = 0
travel_idx = 0
isCorrect = True

if travels[0] != 1:
    isCorrect = False

while st:
    cur, depth = st.pop()

    if cur == travels[travel_idx]:
        visited[cur] = depth+1
        travel_idx += 1
    else:
        isCorrect = False
        break

    for child in sorted(edges[cur], key=lambda x: _order[x], reverse=True):
        if visited[child] != -1:
            continue
        else:
            st.append([child, depth+1])


print(1 if isCorrect else 0)