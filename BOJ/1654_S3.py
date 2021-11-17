def main():
    NK = list(map(int, input().split()))
    N, K = NK[0], NK[1]

    cables = []
    sum_len = 0
    for _ in range(N):
        cables.append(int(input()))
        sum_len += cables[-1]
    
    cables = sorted(cables, reverse=True)
    high = sum_len//K
    low = 1
    while low <= high:
        sum = 0
        mid = (high + low)//2
        for cable in cables:
            sum += cable//mid
            if sum >= K:
                low = mid + 1
                break
        if sum < K:
            high = mid - 1
    print(high)

if __name__ == "__main__":
    main()