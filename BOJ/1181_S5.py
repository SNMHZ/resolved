from functools import cmp_to_key

def main():
    N = int(input())

    words = set()
    for _ in range(N):
        words.add(input())
    
    def cmp(x, y):
        if len(x) != len(y):
            return len(x) - len(y)
        for i in range(len(x)):
            if x[i] != y[i]:
                return ord(x[i]) - ord(y[i])

    for word in sorted(list(words), key=cmp_to_key(cmp)):
        print(word)
    
if __name__ == "__main__":
    main()