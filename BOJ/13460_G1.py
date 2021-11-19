import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [ list(sys.stdin.readline().strip()) for _ in range(N) ]

# Y, X
red_pos, blue_pos, hole = None, None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_pos = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue_pos = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'O':
            hole = (i, j)
result = -1

def expand(q: deque, closed: set, red, blue, depth):
    global board
    # 왼쪽으로 기울이기. X 작은 것 먼저
    first, second = (blue, red) if red[1] > blue[1] else (red, blue)
    # 첫번째 구슬 이동
    while board[first[0]][first[1]-1] == '.':
        first = (first[0], first[1]-1)
    # 구멍에 빠졌는지 확인
    if hole == (first[0], first[1]-1):
        first = (first[0], first[1]-1)
    else:
        board[first[0]][first[1]] = '#'
    # 두번째 구슬 이동
    while board[second[0]][second[1]-1] == '.':
        second = (second[0], second[1]-1)
    # 구멍에 빠졌는지 확인
    if hole == (second[0], second[1]-1):
        second = (second[0], second[1]-1)
    if hole != first:
        board[first[0]][first[1]] = '.'
    # 확장
    if red[1] > blue[1]:
        if (second, first) not in closed:
            q.append((second, first, depth+1))
            closed.add((second, first))
    else:
        if (first, second) not in closed:
            q.append((first, second, depth+1))
            closed.add((first, second))

    # 오른쪽으로 기울이기. X 큰 것 먼저
    first, second = (blue, red) if red[1] < blue[1] else (red, blue)
    # 첫번째 구슬 이동
    while board[first[0]][first[1]+1] == '.':
        first = (first[0], first[1]+1) 
    # 구멍에 빠졌는지 확인
    if hole == (first[0], first[1]+1):
        first = (first[0], first[1]+1) 
    else:
        board[first[0]][first[1]] = '#'
    # 두번째 구슬 이동
    while board[second[0]][second[1]+1] == '.':
        second = (second[0], second[1]+1)
    # 구멍에 빠졌는지 확인
    if hole == (second[0], second[1]+1):
        second = (second[0], second[1]+1)
    if hole != first:
        board[first[0]][first[1]] = '.'
    # 확장
    if red[1] < blue[1]:
        if (second, first) not in closed:
            q.append((second, first, depth+1))
            closed.add((second, first))
    else:
        if (first, second) not in closed:
            q.append((first, second, depth+1))
            closed.add((first, second))

    # 위쪽으로 기울이기. Y 작은 것 먼저
    first, second = (blue, red) if red[0] > blue[0] else (red, blue)
    # 첫번째 구슬 이동
    while board[first[0]-1][first[1]] == '.':
        first = (first[0]-1, first[1])
    # 구멍에 빠졌는지 확인
    if hole == (first[0]-1, first[1]):
        first = (first[0]-1, first[1])
    else:
        board[first[0]][first[1]] = '#'
    # 두번째 구슬 이동
    while board[second[0]-1][second[1]] == '.':
        second = (second[0]-1, second[1])
    # 구멍에 빠졌는지 확인
    if hole == (second[0]-1, second[1]):
        second = (second[0]-1, second[1])
    if hole != first:
        board[first[0]][first[1]] = '.'
    # 확장
    if red[0] > blue[0]:
        if (second, first) not in closed:
            q.append((second, first, depth+1))
            closed.add((second, first))
    else:
        if (first, second) not in closed:
            q.append((first, second, depth+1))
            closed.add((first, second))
    # 아래쪽으로 기울이기. Y 큰 것 먼저
    first, second = (blue, red) if red[0] < blue[0] else (red, blue)
    # 첫번째 구슬 이동
    while board[first[0]+1][first[1]] == '.':
        first = (first[0]+1, first[1])
    # 구멍에 빠졌는지 확인
    if hole == (first[0]+1, first[1]):
        first = (first[0]+1, first[1])
    else:
        board[first[0]][first[1]] = '#'
    # 두번째 구슬 이동
    while board[second[0]+1][second[1]] == '.':
        second = (second[0]+1, second[1])
    # 구멍에 빠졌는지 확인
    if hole == (second[0]+1, second[1]):
        second = (second[0]+1, second[1])
    if hole != first:
        board[first[0]][first[1]] = '.'
    # 확장
    if red[0] < blue[0]:
        if (second, first) not in closed:
            q.append((second, first, depth+1))
            closed.add((second, first))
    else:
        if (first, second) not in closed:
            q.append((first, second, depth+1))
            closed.add((first, second))

q = deque()
q.append((red_pos, blue_pos, 0))
closed = set()

while q:
    c_red, c_blue, depth = q.popleft()
    if c_blue != hole and c_red == hole:
        result = depth
        break
    if depth == 10 or hole == c_blue:
        continue
    else:
        expand(q, closed, c_red, c_blue, depth)

print(result)