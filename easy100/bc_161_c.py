N, K = map(int, input().split())


min = N
while True:
    if N >= K and N % K == 0:
        min = 0
        break
    elif N >= K:
        min = N % K
        N = min
    else:
        N = abs(N - K)
        if min >= N:
            min = N
        else:
            break

print(min)