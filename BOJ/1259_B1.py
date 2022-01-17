import sys

while True:
    inp = sys.stdin.readline().strip()
    if inp == '0':
        break
    isPalindrome = True

    for i in range(len(inp) // 2):
        if inp[i] != inp[-i - 1]:
            isPalindrome = False
            break

    print('yes' if isPalindrome else 'no')