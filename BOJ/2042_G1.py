import sys

N, M, K = map(int, sys.stdin.readline().split())
nums = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
oper = [ list(map(int, sys.stdin.readline().split())) for _ in range(M+K) ]

size = 1
while size < N:
    size <<= 1
segTree = [0] * (size << 1)

def build_segTree(start, end, node):
    if start == end:
        segTree[node] = nums[start]
        return nums[start]
    mid = (start + end) >> 1
    left = build_segTree(start, mid, node << 1)
    right = build_segTree(mid+1, end, (node << 1) + 1)
    segTree[node] = left + right
    return segTree[node]

def update_segTree(start, end, idx, val, node=1):
    if start == end:
        segTree[node] = val
        return
    mid = (start + end) >> 1
    if idx <= mid:
        update_segTree(start, mid, idx, val, node << 1)
    else:
        update_segTree(mid+1, end, idx, val, (node << 1) + 1)
    segTree[node] = segTree[node << 1] + segTree[(node << 1) + 1]

def sum_segTree(start, end, l, r, node=1):
    if start > end or start > r or end < l:
        return 0
    if l <= start and end <= r:
        return segTree[node]
    mid = (start + end) >> 1
    return sum_segTree(start, mid, l, r, node << 1) + sum_segTree(mid+1, end, l, r, (node << 1) + 1)

build_segTree(0, N-1, 1)

for a, b, c in oper:
    # 변경
    if a == 1:
        nums[b-1] = c
        update_segTree(0, N-1, b-1, c, 1)
    # 출력
    else:
        print(sum_segTree(0, N-1, b-1, c-1, 1))