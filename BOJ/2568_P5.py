import sys

N = int(sys.stdin.readline())
_arr = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: x[0])
m_dict = dict([ (x[1], x[0]) for x in _arr ])
arr = [ a[1] for a in _arr ]


lis = [ arr[0] ]
count = 1
path_idx = [0]

for i in range(1, N):
    if arr[i] > lis[-1]:
        path_idx.append(len(lis))
        lis.append(arr[i])
        count += 1
    else:
        left = 0
        right = len(lis) - 1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        path_idx.append(left)
        lis[left] = arr[i]

print(len(arr) - count)

path = []
count-=1
for i in range(N - 1, -1, -1):
    if path_idx[i] == count:
        path.append(arr[i])
        count -= 1
        continue

# for p in path[::-1]:
#     print(p, end=' ')

res = []
for p in path:
    if p in m_dict:
        m_dict[p] = -1

for k in m_dict:
    if m_dict[k] != -1:
        res.append(m_dict[k])
print( '\n'.join(map(str, res)) )