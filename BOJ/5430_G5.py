def func_R(toFront:bool, count:int) -> bool:
    if count%2 == 0:
        return toFront
    return not toFront

def func_D(toFront:bool, start:int, end:int, count:int):
    if toFront:
        return start+count, end
    return start, end-count

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()[:-1]
    n = int(sys.stdin.readline()[:-1])
    if n == 0:
        sys.stdin.readline()
        if 'D' in p:
            print('error')
            continue
        else:
            print('[]')
            continue
    arr = list(map(int, sys.stdin.readline()[1:-2].split(',')))

    instructions = []
    cur, count = p[0], 1
    count_D = 0
    for c in p[1:]:
        if cur == c:
            count += 1
        else:
            instructions.append((cur, count))
            if cur == 'D':
                count_D += count
            cur, count = c, 1
    instructions.append((cur, count))
    if cur == 'D':
        count_D += count

    if count_D > n:
        print('error')
        continue
    elif count_D == n:
        print('[]')
        continue

    start, end = 0, len(arr)-1
    toFront = True

    for i in range(len(instructions)):
        cur, count = instructions[i]
        if cur == 'R':
            toFront = func_R(toFront, count)
        elif cur == 'D':
            start, end = func_D(toFront, start, end, count)

    if toFront:
        print('[', end='')
        for i in range(start, end):
            print(f'{arr[i]}', end=',')
        print(f'{arr[end]}]')
    else:
        print('[', end='')
        for i in range(end, start, -1):
            print(f'{arr[i]}', end=',')
        print(f'{arr[start]}]')