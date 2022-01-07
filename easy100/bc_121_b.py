import math
import itertools

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for l in range(N)]

c = 0
for i in range(N):
    for j in range(M):
        if j == 0:
            score = A[i][j] * B[j]
        else:
            score += A[i][j] * B[j]

    score += C
    if score > 0:
        c += 1

print(c)