import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

_min = float('inf')
_minpos = []

for i in range(N-2):
    left, right = i+1, N-1

    _sum = data[left] + data[right] + data[i]
    if abs(_sum) < _min:
        _min = abs(_sum)
        _minpos = [i, left, right]
    while left < right:
        _sum = data[left] + data[right] + data[i]
        if abs(_sum) < _min:
            _min = abs(_sum)
            _minpos = [i, left, right]

        if _sum < 0:
            left += 1
        elif _sum > 0:
            right -= 1
        else:
            break

print(data[_minpos[0]], data[_minpos[1]], data[_minpos[2]])