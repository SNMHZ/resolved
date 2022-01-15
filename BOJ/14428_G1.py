import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
oper = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

size = 1
while size < N:
    size <<= 1
segTree = [0] * (size << 1)

def get_min_idx(left, right):
    return left if left[0] <= right[0] else right

def build_segTree(start, end, node):
    if start == end:
        segTree[node] = (arr[start], start)
        return segTree[node]
    mid = (start + end) >> 1
    left = build_segTree(start, mid, node << 1)
    right = build_segTree(mid+1, end, (node << 1) + 1)
    segTree[node] = get_min_idx(left, right)
    return segTree[node]

def update_segTree(start, end, idx, val, node=1):
    if start == end:
        segTree[node] = (val, idx)
        return
    mid = (start + end) >> 1
    if idx <= mid:
        update_segTree(start, mid, idx, val, node << 1)
    else:
        update_segTree(mid+1, end, idx, val, (node << 1) + 1)
    segTree[node] = get_min_idx(segTree[node << 1], segTree[(node << 1) + 1])

def quarry_segTree(start, end, l, r, node=1):
    if start > end or start > r or end < l:
        return (float('inf'), None)
    if l <= start and end <= r:
        return segTree[node]
    mid = (start + end) >> 1
    return  get_min_idx(quarry_segTree(start, mid, l, r, node << 1), quarry_segTree(mid+1, end, l, r, (node << 1) + 1))

build_segTree(0, N-1, 1)

for a, b, c in oper:
    # 변경
    if a == 1:
        arr[b-1] = c
        update_segTree(0, N-1, b-1, c, 1)
    # 출력
    else:
        print(quarry_segTree(0, N-1, b-1, c-1, 1)[1]+1)