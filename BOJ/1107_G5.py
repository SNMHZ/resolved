import sys

N = sys.stdin.readline()[:-1]
sys.stdin.readline()
disables = sys.stdin.readline().split()

minimum = abs(int(N)-100)

low, high = None, None
for i in range(10):
    if str(i) not in disables:
        low = i
        break
for i in range(9, -1, -1):
    if str(i) not in disables:
        high = i
        break

m_str = ''
for c in N:
    if c not in disables:
        m_str+=c
    else:
        cur = c
        check_big = m_str
        while cur != '9':
            cur = chr(ord(cur)+1)
            if cur not in disables:
                check_big+=cur
                check_big+=(len(N)-len(check_big))*str(low)
                print(check_big)
                break
        if c == '9':
            

        break
    
    print(c)

print(N, disables)