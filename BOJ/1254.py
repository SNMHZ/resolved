import sys

inp = sys.stdin.readline().strip()

def isPalindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

for i in range(len(inp)):
    if isPalindrome(inp+inp[:i][::-1]):
        print(len(inp)+i)
        break