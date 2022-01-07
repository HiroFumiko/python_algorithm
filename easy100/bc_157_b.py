A = [list(map(int, input().split())) for l in range(3)]
N = int(input())
B = [int(input()) for l in range(N)]

card = [[0 for _ in range(3)] for i in range(3)]

for i in range(N):
    for j in range(3):
        if B[i] in A[j]:
            idx = A[j].index(B[i])
            card[j][idx] += 1

if (card[0][0] + card[0][1] + card[0][2] == 3 or
    card[1][0] + card[1][1] + card[1][2] == 3 or
    card[2][0] + card[2][1] + card[2][2] == 3 or
    card[0][0] + card[1][0] + card[2][0] == 3 or
    card[0][1] + card[1][1] + card[2][1] == 3 or
    card[0][2] + card[1][2] + card[2][2] == 3 or
    card[0][0] + card[1][1] + card[2][2] == 3 or
    card[2][0] + card[1][1] + card[0][2] == 3):
    ans = True
else:
    ans = False


print('Yes') if ans else print('No')