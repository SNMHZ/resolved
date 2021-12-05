import sys

board = [ sys.stdin.readline().strip() for _ in range(10) ]

for k, row in enumerate(board):
    bit = 0
    for i in range(10):
        if row[i] == 'O':
            bit |= 1 << i
    board[k] = bit

def toggle_light(board, y, x):
    #위
    if y > 0:
        board[y-1] ^= 1 << x
    
    #중간
    board[y] ^= 1 << x
    if x > 0:
        board[y] ^= 1 << (x-1)
    if x < 9:
        board[y] ^= 1 << (x+1)
    
    #아래
    if y < 9:
        board[y+1] ^= 1 << x

res = float('inf')
for mask in range(1 << 10):
    board_copy = board.copy()
    count = 0
    for x in range(10):
        if mask & (1 << x):
            count += 1
            toggle_light(board_copy, 0, x)

    for y in range(1, 10):
        for x in range(10):
            if board_copy[y-1] & (1 << x):
                count += 1
                toggle_light(board_copy, y, x)

    if board_copy[9] == 0:
        res = min(res, count)

print(res if res != float('inf') else -1)