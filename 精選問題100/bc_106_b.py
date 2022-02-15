N = int(input())

res = 0
for i in range(1, N+1):
    if i % 2 == 1:
        c = 0
        for j in range(1, 201):
            if i % j == 0 and i >= j:
                c += 1

        if c == 8:
            res += 1

print(res)