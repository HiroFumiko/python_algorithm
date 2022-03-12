N = int(input())
D, X = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

choco_count = 0

for a in A:
    i = 1
    eat_day = 1
    while D >= eat_day:
        eat_day = i*a + 1
        choco_count += 1
        i += 1

ans = choco_count + X
print(ans)


