import sys

N, M = map(int, sys.stdin.readline().split())
nums = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
oper = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]

size = 1
while size < N:
    size <<= 1
segTree = [0] * (size << 1)

def get_minmax(left, right):
    return (min(left[0], right[0]), max(left[1], right[1]))

def build_segTree(start, end, node):
    if start == end:
        segTree[node] = (nums[start], nums[start])
        return segTree[node]
    mid = (start + end) >> 1
    left = build_segTree(start, mid, node << 1)
    right = build_segTree(mid+1, end, (node << 1) + 1)
    segTree[node] = get_minmax(left, right)
    return segTree[node]

# def update_segTree(start, end, idx, val, node=1):
#     if start == end:
#         segTree[node] = val
#         return
#     mid = (start + end) >> 1
#     if idx <= mid:
#         update_segTree(start, mid, idx, val, node << 1)
#     else:
#         update_segTree(mid+1, end, idx, val, (node << 1) + 1)
#     segTree[node] = segTree[node << 1] * segTree[(node << 1) + 1] % mod

def quarry_segTree(start, end, l, r, node=1):
    if start > end or start > r or end < l:
        return (float('inf'), float('-inf'))
    if l <= start and end <= r:
        return segTree[node]
    mid = (start + end) >> 1
    return  get_minmax(quarry_segTree(start, mid, l, r, node << 1), quarry_segTree(mid+1, end, l, r, (node << 1) + 1))

build_segTree(0, N-1, 1)

for a, b in oper:
    print(*quarry_segTree(0, N-1, a-1, b-1, 1))