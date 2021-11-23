import sys

N = int(sys.stdin.readline())
board = [ [0] * N for _ in range(N) ]

count = 0
st = [ [i] for i in range(N) ]

def get_valid(cur):
    l = len(cur)
    res = 0
    for i in range(l):
        res = res | (1 << cur[i])
        res = res | (1 << (cur[i] + l - i))
        if cur[i]-l+i>=0:
            res = res | (1 << (cur[i] - l + i))
    return [ i for i in range(N) if not res & (1 << i) ]

while st:
    cur = st.pop()
    if len(cur) == N:
        #print(cur)
        count += 1
        continue
    valid = get_valid(cur)
    for i in valid:
        st.append(cur + [i])
print(count)