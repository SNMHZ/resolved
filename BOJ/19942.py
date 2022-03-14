import sys

N = int(sys.stdin.readline())
mp, mf, ms, mv = map(int, sys.stdin.readline().split())
datas = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]


min_val, min_path = float('inf'), None
st = [ (i, 1<<i, *datas[i]) for i in range(N-1, -1, -1) ]

for i in range(N):
    start, path, p, f, s, v, val = st[i]
    print(bin(path), p, f, s, v, val)

while st: 
    start, path, p, f, s, v, val = st.pop()
    print(bin(path))
    if p >= mp and f >= mf and s >= ms and v >= mv:
        if val < min_val:
            min_val = val
            min_path = path
        # continue

    for i in range(N-1, start-1, -1):
        if (path>>i)&1:
            continue
        if val+datas[i][0] < min_val:
            st.append((start, path|(1<<i), p+datas[i][0], f+datas[i][1], s+datas[i][2], v+datas[i][3], val+datas[i][4]))


if min_path is None:
    print(-1)
else:
    print(min_val)
    print(*[i+1 for i in range(N) if (min_path>>i)&1])
