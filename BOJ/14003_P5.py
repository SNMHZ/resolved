import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

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

print(count)

path = []
count-=1
for i in range(N - 1, -1, -1):
    if path_idx[i] == count:
        path.append(arr[i])
        count -= 1
        continue

for p in path[::-1]:
    print(p, end=' ')