row1, row2 = 'WBWBWBWB', 'BWBWBWBW'
board1, board2 = [ row1, row2 ]*4, [ row2, row1 ]*4

def compare_board(correct, board, x, y):
    n=0
    for i in range(8):
        for j in range(8):
            if correct[i][j] != board[x+i][y+j]:
                n+=1
    return n

def main():
    MN = list(map(int, input().split()))
    M, N = MN[0], MN[1]

    board = []
    for i in range(M):
        board.append(input())
    
    to_change_list = []
    for i in range(M-7):
        for j in range(N-7):
            to_change_list.append(compare_board(board1, board, i, j))
            to_change_list.append(compare_board(board2, board, i, j))
    print(min(to_change_list))

if __name__ == "__main__":
    main()