# C로 다시 짜고 싶은 충동을 이겨냈다..
import sys
from collections import deque

board = [ list(map(int, sys.stdin.readline().split())) for _ in range(9)]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    
    for i in range(9):
        if board[i][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            if board[row//3*3+i][col//3*3+j] == num:
                return False

    return True


blanks = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            res = ''
            for k in range(1, 10):
                if is_valid(board, i, j, k):
                    res+=str(k)
            blanks.append((i, j, res))

q = deque()
q.append( (0, '') )

before = -1
while q:
    index, n = q.pop()

    if before >= index:
        for i in range(index):
            board[blanks[i][0]][blanks[i][1]] = int(n[i])
        for i in range(index, before+1):
            board[blanks[i][0]][blanks[i][1]] = 0

    if len(blanks) == index:
        break

    i, j, p = blanks[index]
    for k in p:
        if is_valid(board, i, j, int(k)):
            board[blanks[index][0]][blanks[index][1]] = int(k)
            q.append( (index+1, n+k) )
    before = index

print('\n'.join([' '.join(map(str, b)) for b in board]))