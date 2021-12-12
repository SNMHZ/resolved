import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split())) 

half_idx = N // 2
left_dict = {}
ans = 0

st = [ (arr[0], 1), (0, 1) ]
while st:
    cur, depth = st.pop()
    if depth >= half_idx:
        left_dict[cur] = left_dict.get(cur, 0) + 1
    else:
        st.append((cur, depth+1))
        st.append((cur + arr[depth], depth+1))

st = [ (arr[half_idx], half_idx+1), (0, half_idx+1) ]
while st:
    cur, depth = st.pop()
    if depth >= N:
        ans += left_dict.get(S-cur, 0)
    else:
        st.append((cur, depth+1))
        st.append((cur + arr[depth], depth+1))

if S == 0:
    ans -= 1

if N == 1:
    if S == arr[0]:
        ans = 1
    else:
        ans = 0

print(ans)