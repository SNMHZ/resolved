import sys
import heapq

N = int(sys.stdin.readline())
lessons = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
rooms = []

lessons.sort(key=lambda x: x[0])

for i in range(N):
    if len(rooms) != 0 and rooms[0] <= lessons[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, lessons[i][1])

print(len(rooms))