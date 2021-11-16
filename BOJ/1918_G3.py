import sys
from collections import deque

line = sys.stdin.readline()[:-1]

def middle_to_postfix(middle):
    st = deque()
    res = ''

    for i in middle:
        if i == '+' or i == '-':
            while st and st[-1] != '(':
                res += st.pop()
            st.append(i)
        elif i == '*' or i == '/':
            while st and st[-1] != '(' and st[-1] != '+' and st[-1] != '-':
                res += st.pop()
            st.append(i)
        elif i == '(':
            st.append(i)
        elif i == ')':
            while st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            res += i

    while st:
        res += st.pop()

    return res
    

print(middle_to_postfix(line))