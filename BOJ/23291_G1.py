#으악 귀찮아
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

snail_map = [[-1] * N for _ in range(N)]
snail_idx = [None] * N
for i in range(N):
    snail_map[0][i] = i

offset = 0
oy, ox = 1, 1

while oy <= (N-oy*ox):
    print(offset)
    for i in range(ox):
        for j in range(oy):
            snail_map[ox-i][offset+ox+j] = snail_map[j][offset+i]
            snail_map[j][offset+i] = -1
    offset+=ox
    oy, ox = ox+1, oy

for y in range(oy):
    for x in range(offset, N):
        if snail_map[y][x] != -1:
            snail_idx[snail_map[y][x]] = [y, x]
snail_map[0] = arr

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
snail_mod = [ [0]*N for _ in range(N) ]
def snail_fish():
    for k, (y, x) in enumerate(snail_idx):
        snail_map[y][x] = snail_map[0][k]
        if y != 0:
            snail_map[0][k] = -1
    
    for y in range(oy):
        for x in range(offset, N):
            if snail_map[y][x] != -1:
                print(snail_map[y][x])
                for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ny, nx = y+dy, x+dx
                    if nx<N and snail_map[ny][nx] != -1:
                        cur_mod = abs(snail_map[ny][nx]-snail_map[y][x])//5
                        cur_mod *= (1 if snail_map[ny][nx] > snail_map[y][x] else -1)
                        snail_mod[y][x] += cur_mod
    for y in range(oy):
        for x in range(offset, N):
            snail_map[y][x] += snail_mod[y][x]
            snail_mod[y][x] = 0

    print()
    for row in snail_mod:
        print(row)

    print()
    for row in snail_map:
        print(row)


# 절반 두번 쌓기 & 정리 & 펼치기
def half_fish():
    pass

# 차이 K 이하인지 체크
count = 0
while True:
    if max(arr) - min(arr) <= K:
        break
    count += 1
    add_fish()
    snail_fish()
    half_fish()
    break

print(count)

