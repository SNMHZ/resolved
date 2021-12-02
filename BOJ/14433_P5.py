import sys

N, M, K1, K2 = map(int, sys.stdin.readline().split())

team1 = [ [] for _ in range(N) ]
team2 = [ [] for _ in range(N) ]
for _ in range(K1):
    a, b = map(int, sys.stdin.readline().split())
    team1[a-1].append(b-1)
for _ in range(K2):
    a, b = map(int, sys.stdin.readline().split())
    team2[a-1].append(b-1)

def bipartite_matching(vectors, N, M):
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
    for i in range(N):
        if L[i] == -1:
            visited = [False] * N
            if dfs(i, visited):
                match += 1

    return match

if bipartite_matching(team1, N, M) < bipartite_matching(team2, N, M):
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')