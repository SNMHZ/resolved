# https://seongonion.tistory.com/43
# 에라토스테네스의 체
# 소수 판별은 그냥 검색할래..
# 히든케이스 항상 생각하기

def is_prime_num(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr


def main():
    LH = list(map(int, input().split()))
    low, high = LH[0] if LH[0] > 2 else 2, LH[1]

    arr = is_prime_num(high)

    for i in range(low, len(arr)):
        if arr[i]:
            print(i)


if __name__ == "__main__":
    main()