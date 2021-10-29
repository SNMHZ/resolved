# 코파일럿은 꽤나 똑똑하다.
# 하지만 쓰는 사람도 정확히 자기가 뭘 만드려는지 알아야 한다.
# 주석 달고있는것도 자동완성을 자꾸 해 대니 참 GPT는 기가 막히네...
# 얘는 그저 내가 뜻하고자 하는 것을 예측하지는 못하고, 가장 그럴듯한 것을 예측(학습된 것 기반으로)할 뿐이다.
# 지금 이렇게 주석을 달아주고 있을 때에도 그럴듯한 문장 자체는 되게 잘 만든다.
# 하지만 절대 내 의도 자체를 예측하지는 못하는 듯.
# 인공지능은 창조적이지 못하다 라는 사실이 굉장히 와닿는다.
# 알고리즘을 짤 때는 인공지능에 의존하지 않는 것이 좋을 것 같다.
# 다만 매우 예측가능한 코드만 남아 작성할 때에는 간결하고 효율적인 코드를 자동완성 해 주니 편하다.
# 잘만 쓰면 굉장히 생산성이 높을 것 같은데, 굳이 익숙해 지고 싶지 않은 불쾌함?이 조금 느껴지는 듯.

import sys

N, M = map(int, sys.stdin.readline().split())
maze = [ sys.stdin.readline()[:M] for _ in range(N)]

# input
# 4 6
# 101111
# 101010
# 101011
# 111011
# output
# 15

# '1' is road, '0' is wall
# start from (0, 0) to (N-1, M-1) 
#find the shortest path depth and print it

def bfs(maze, x=0, y=0, depth = 0):
    st = [(x, y, depth)]
    visited = [[False]*M for _ in range(N)]
    visited[x][y] = True
    while st:
        x, y, depth = st.pop(0)
        if x == N-1 and y == M-1:
            return depth
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maze[nx][ny] == '1':
                st.append((nx, ny, depth+1))
                visited[nx][ny] = True
                visited[N-1][M-1] = False
    return -1

print(bfs(maze, 0, 0, 1))