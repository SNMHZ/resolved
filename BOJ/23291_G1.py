#으악 귀찮아~
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(arr)

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
def snail_fish():
    pass

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

print(count)

