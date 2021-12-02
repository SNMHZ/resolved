import sys

N, M, K = map(int, sys.stdin.readline().split())
vectors = [ list(map(lambda x:int(x)-1, sys.stdin.readline().split()))[1:] for _ in range(N) ]

def bipartite_matching(vectors, N, M, K):
    L = [-1] * N
    R = [-1] * M

    def dfs(here, visited) -> bool:
        if visited[here]:
            return False
        visited[here] = True
        for there in vectors[here]:
            if R[there] == -1 or (not visited[R[there]] and dfs(R[there], visited)):
                L[here] = there
                R[there] = here
                return True
        return False

    match = 0
    for i in range(N//2):
        if L[i] == -1:
            visited = [False] * (N//2)
            if dfs(i, visited):
                match += 1

    for i in range(N):
        if L[i] == -1:
            visited = [False] * N
            if dfs(i, visited):
                match += 1
                K -= 1
                if K == 0:
                    break

    return match

print(bipartite_matching(vectors*2, N*2, M, K))