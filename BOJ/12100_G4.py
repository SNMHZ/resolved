#2048 으익 귀찮아~
import sys

N = int(sys.stdin.readline())
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

print(board)