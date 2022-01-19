import sys

N, d = map(int, sys.stdin.readline().split())


cur = N+1
if cur <= d**(d-1):
    cur = d**(d-1)

while True:
    m_list = []
    n = cur
    while n//d:
        m_list.append(n%d)
        n = n//d
    m_list.append(n)
    isAll = True
    if len(m_list) == d:
        check = [True]*d
        for i in m_list:
            if check[i]:
                check[i] = False
            else:
                isAll = False
                break
    else:
        cur = -1
        break

    if isAll:
        break

    cur += 1

print(cur)