import sys

R, C = map(int, sys.stdin.readline().split())
board = [ list(sys.stdin.readline().strip()) for _ in range(R) ]
visited = [ [0]*C for _ in range(R) ]

max_depth = 0
def loc(y, x):
    return 1<<(ord(board[y][x])-65)

st = [  (0, 0, loc(0,0), 1) ]

while st:
    y, x, mask, depth = st.pop()
    if depth > max_depth:
        max_depth = depth
    if depth == 26:
        break
    
    for dy, dx in ( (1, 0), (-1, 0), (0, 1), (0, -1) ):
        ny, nx = y+dy, x+dx
        if 0 <= ny < R and 0 <= nx < C and not mask&loc(ny, nx): # 범위 내에 있고, 방문하지 않았다면
            # print(ny, nx, bin(visited[ny][nx]), bin(mask), bin(loc(ny, nx)), (mask|loc(ny, nx)), depth+1)
            if visited[ny][nx] != (mask|(loc(ny, nx))): #방문한 알파벳이 완전히 똑같은 경우(순서 상관 없음) 제외
                visited[ny][nx] = (mask|(loc(ny, nx)))
                st.append( ( ny, nx, mask|loc(ny, nx) , depth+1 ) )

print(max_depth)