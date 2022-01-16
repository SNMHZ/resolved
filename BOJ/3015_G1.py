import sys

N = int(sys.stdin.readline())
arr = [ int(sys.stdin.readline().strip()) for _ in range(N) ]

st = []
count = 0

for i in range(N):
    nu = 1
    while st and st[-1][0] <= arr[i]:
        count += st[-1][1]
        if st[-1][0] == arr[i]:
            nu = st[-1][1] + 1
        else:
            nu = 1
        st.pop()
    if st:
        count += 1
    st.append((arr[i], nu))

print(count)