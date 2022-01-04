import sys
sys.setrecursionlimit(250000)

def find(x, parent: list, weights: list):
    if parent[x] == -1:
        return x
    p = find(parent[x], parent, weights)
    weights[x] += weights[parent[x]]
    parent[x] = p
    return parent[x]

def union(x, y, w, parent: list, weights: list):
    root_x = find(x, parent, weights)
    root_y = find(y, parent, weights)
    if root_x == root_y:
        return
    
    weights[root_y] = weights[x] - weights[y] + w
    parent[root_y] = root_x

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    
    weights = [0] * (N+1)
    parent = [-1] * (N+1)

    for _ in range(M):
        inp = sys.stdin.readline().split()
        if inp[0] == '!':
            a, b, w = int(inp[1]), int(inp[2]), int(inp[3])
            union(a, b, w, parent, weights)
        else:
            a, b = int(inp[1]), int(inp[2])
            if find(a, parent, weights) == find(b, parent, weights):
                print(weights[b]-weights[a])
            else:
                print('UNKNOWN')