N = int(input())
query = [0 for i in range(45)]

for i in range(N+1):
    if i == 0 or i == 1:
        query[i] = 1
    else:
        query[i] = query[i - 1] + query[i - 2]

print(query[N])