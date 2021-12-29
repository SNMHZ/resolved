import sys

segTree = []
nums = []

def build_segTree(start, end, node):
    if start == end:
        if nums[start] < 0:
            nums[start] = -1
        elif nums[start] > 0:
            nums[start] = 1
        segTree[node] = nums[start]
        return nums[start]
    mid = (start + end) >> 1
    segTree[node] = build_segTree(start, mid, node << 1) * build_segTree(mid+1, end, (node << 1) + 1)
    return segTree[node]

def update_segTree(start, end, idx, val, node=1):
    if idx < start or end < idx:
        return
    if start == end:
        segTree[node] = val
        return
    mid = (start + end) >> 1
    update_segTree(start, mid, idx, val, node << 1)
    update_segTree(mid+1, end, idx, val, (node << 1) + 1)
    segTree[node] = segTree[node << 1] * segTree[(node << 1) + 1]

def quarry_segTree(start, end, l, r, node=1):
    if r < start or end < l:
        return 1
    if l <= start and end <= r:
        return segTree[node]
    mid = (start + end) >> 1
    return quarry_segTree(start, mid, l, r, node << 1) * quarry_segTree(mid+1, end, l, r, (node << 1) + 1)

while True:
    try:
        N, K = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        oper = [ sys.stdin.readline().split() for _ in range(K) ]

        size = 1
        while size < N:
            size <<= 1
        segTree = [0] * (size << 1)

        build_segTree(0, N-1, 1)

        for a, b, c in oper:
            b, c = map(int, [b, c])
            # 변경
            if a == 'C':
                if c < 0:
                    c = -1
                elif c > 0:
                    c = 1
                nums[b-1] = c
                update_segTree(0, N-1, b-1, c, 1)
            # 출력
            else:
                res = quarry_segTree(0, N-1, b-1, c-1, 1)
                if res < 0:
                    print('-', end='')
                elif res == 0:
                    print('0', end='')
                else:
                    print('+', end='')
        print()
    except Exception:
        break