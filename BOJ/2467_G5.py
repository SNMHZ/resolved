import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

left, right = 0, N-1
_sum = data[left] + data[right]
_min = abs(_sum)
_minpos = [left, right]
while left < right:
    _sum = data[left] + data[right]
    if abs(_sum) < _min:
        _min = abs(_sum)
        _minpos = [left, right]

    if _sum < 0:
        left += 1
    elif _sum > 0:
        right -= 1
    else:
        break

print(data[_minpos[0]], data[_minpos[1]])

# def bin_search(to_find):
#     left, right = 0, len(data)-1
#     while left < right:
#         mid = (left+right)//2
#         if data[mid] > to_find:
#             right = mid - 1
#         elif data[mid] < to_find:
#             left = mid + 1
#         else:
#             return mid
#     return left

# val = abs(data[0] + data[-1])
# res = (0, N-1)
# for i in range(N):
#     to_find = -data[i]
#     idx = bin_search(to_find)

#     d1, d2 = abs(data[i] + data[idx]), float('inf')
#     if idx != 0:
#         d2 = abs(data[i] + data[idx-1])

#     # print(i)
#     # print(val, res)
#     # print(d1, (i, idx))
#     # print(d2, (i, idx-1))
#     # print()
#     if val > d1 and i != idx:
#         val = d1
#         res = (i, idx)
#     if val > d2 and i != idx-1:
#         val = d2
#         res = (i, idx-1)

# print( *sorted([data[res[0]], data[res[1]]]))