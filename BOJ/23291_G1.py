import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

board = [[-1] * N for _ in range(N)]
snail_idx = [None] * N
half_idx = [None] * N

# snail_fish() init
for i in range(N):
    board[0][i] = i
s_offset = 0
sy, sx = 1, 1
while sy <= (N-sy*sx):
    for y in range(sy):
        for x in range(sx):
            board[sx-x][s_offset+sx+y] = board[y][s_offset+x]
            board[y][s_offset+x] = -1
    s_offset+=sx
    sy, sx = sx+1, sy
for y in range(sy):
    for x in range(s_offset, N):
        if board[y][x] != -1:
            snail_idx[board[y][x]] = [y, x]
            board[y][x] = -1

# half_fish() init
for i in range(N):
    board[0][i] = i
h_offset = 0
hy, hx = 1, N//2
for i in range(2):
    for y in range(hy):
        for x in range(hx):
            board[(hy*2)-1-y][N-1-x] = board[y][h_offset+x]
            board[y][h_offset+x] = -1
    h_offset+=hx
    hy, hx = hy*2, hx//2
for y in range(hy):
    for x in range(h_offset, N):
        if board[y][x] != -1:
            half_idx[board[y][x]] = [y, x]
            board[y][x] = -1

board[0] = arr

# 젤 적은거에 하나씩
def add_fish():
    _min, _min_idx = arr[0], [0]
    for i in range(1, N):
        if arr[i] < _min:
            _min, _min_idx = arr[i], [i]
        elif arr[i] == _min:
            _min_idx.append(i)
    for i in _min_idx:
        arr[i] += 1

# 달팽이 만들기 & 정리 & 펼치기
mod_board = [ [0]*N for _ in range(N) ]
def snail_fish():
    #  달팽이 만들기
    for k, (y, x) in enumerate(snail_idx):
        board[y][x] = board[0][k]
        if y != 0:
            board[0][k] = -1
    # 정리
    for y in range(sy):
        for x in range(s_offset, N):
            if board[y][x] != -1:
                for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ny, nx = y+dy, x+dx
                    if 0<=nx<N and 0<=ny<N and board[ny][nx] != -1:
                        cur_mod = abs(board[ny][nx]-board[y][x])//5
                        cur_mod *= (1 if board[ny][nx] > board[y][x] else -1)
                        mod_board[y][x] += cur_mod
    for y in range(sy):
        for x in range(s_offset, N):
            board[y][x] += mod_board[y][x]
            mod_board[y][x] = 0
    # 펼치기
    for y in range(sy):
        for x in range(s_offset, s_offset+sx):
            board[0][(x-s_offset)*sy+y] = board[y][x]
            board[y][x] = -1

# 절반 두번 쌓기 & 정리 & 펼치기
def half_fish():
    # 절반 두번 쌓기
    for k, (y, x) in enumerate(half_idx):
        board[y][x] = board[0][k]
        if y != 0:
            board[0][k] = -1
    # 정리
    for y in range(hy):
        for x in range(h_offset, N):
            if board[y][x] != -1:
                for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ny, nx = y+dy, x+dx
                    if 0<=nx<N and 0<=ny<N and board[ny][nx] != -1:
                        cur_mod = abs(board[ny][nx]-board[y][x])//5
                        cur_mod *= (1 if board[ny][nx] > board[y][x] else -1)
                        mod_board[y][x] += cur_mod
    for y in range(hy):
        for x in range(h_offset, N):
            board[y][x] += mod_board[y][x]
            mod_board[y][x] = 0
    # 펼치기
    for y in range(hy):
        for x in range(h_offset, N):
            board[0][(x-h_offset)*hy+y] = board[y][x]
            board[y][x] = -1

# 차이 K 이하인지 체크
count = 0
while True:
    if max(arr) - min(arr) <= K:
        break
    count += 1
    add_fish()
    snail_fish()
    half_fish()

print(count)