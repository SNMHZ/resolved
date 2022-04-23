import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

OFFSET = max(map(abs, [r1, c1, r2, c2]))
size_y = abs(r1-r2)+1 
size_x = abs(c1-c2)+1 
board = [[0] * size_x for _ in range(size_y)]


def fill_row(y, sx, ex, num):
    if sx > ex:
        for x in range(sx, ex, -1):
            if r1 <= y-OFFSET <= r2 and c1 <= x-OFFSET <= c2:
                board[y-OFFSET-r1][x-OFFSET-c1] = num
            num += 1
        return
    
    for x in range(sx, ex):
        if r1 <= y-OFFSET <= r2 and c1 <= x-OFFSET <= c2:
            board[y-OFFSET-r1][x-OFFSET-c1] = num
        num += 1

def fill_col(x, sy, ey, num):
    if sy > ey:
        for y in range(sy, ey, -1):
            if r1 <= y-OFFSET <= r2 and c1 <= x-OFFSET <= c2:
                board[y-OFFSET-r1][x-OFFSET-c1] = num
            num += 1
        return

    for y in range(sy, ey):
        if r1 <= y-OFFSET <= r2 and c1 <= x-OFFSET <= c2:
            board[y-OFFSET-r1][x-OFFSET-c1] = num
        num += 1

def fill_shell(i):
    num = (1 + 2*(i-1))**2 + 1
    move_n = 2*i
    cur_y, cur_x = OFFSET+i-1, OFFSET+i-1

    # 오른
    cur_x = cur_x + 1
    fill_col(cur_x, cur_y, cur_y-move_n, num)
    cur_y = cur_y - move_n + 1
    num += move_n

    # 위
    cur_x = cur_x - 1
    fill_row(cur_y, cur_x, cur_x-move_n, num)
    cur_x = cur_x - move_n + 1
    num += move_n

    # 왼
    cur_y = cur_y + 1
    fill_col(cur_x, cur_y, cur_y+move_n, num)
    cur_y = cur_y + move_n - 1
    num += move_n

    # 아래
    cur_x = cur_x + 1
    fill_row(cur_y, cur_x, cur_x+move_n, num)
    cur_x = cur_x + move_n - 1

## main
if r1 <= 0 <= r2 and c1 <= 0 <= c2:
            board[-r1][-c1] = 1

for i in range(1, OFFSET+1):
    fill_shell(i)


_max = max([board[0][0], board[0][-1], board[-1][0], board[-1][-1]])
digit = len(str(_max))

for y in range(len(board)):
    for x in range(len(board[0])):
        print(str(board[y][x]).rjust(digit), end=' ')
    print()