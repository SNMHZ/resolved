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
        if 0 <= ny < R and 0 <= nx < C and not mask&loc(ny, nx):
            if visited[ny][nx] ^ (mask|(loc(ny, nx))):
                visited[ny][nx] = (mask|(loc(ny, nx)))
                st.append( ( ny, nx, mask|(loc(ny, nx) ), depth+1 ) )

print(max_depth)