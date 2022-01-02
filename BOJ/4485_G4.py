import sys
import heapq

TC = 0
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    TC += 1

    board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

    dist = [float('inf')] * (N * N)
    dist[0] = board[0][0]

    hq = []
    heapq.heappush(hq, (board[0][0], 0))
    while hq:
        cost, idx = heapq.heappop(hq)
        if idx == N * N - 1:
            break
        for dy, dx in((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny = idx // N + dy
            nx = idx % N + dx
            if 0 <= ny < N and 0 <= nx < N and dist[ny * N + nx] > cost + board[ny][nx]:
                dist[ny * N + nx] = cost + board[ny][nx]
                heapq.heappush(hq, (dist[ny * N + nx], ny * N + nx))

    print('Problem {}: {}'.format(TC, dist[-1]))