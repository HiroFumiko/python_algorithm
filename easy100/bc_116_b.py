def func(x):
    if x % 2 == 0:
        return x / 2
    elif x % 2 == 1:
        return 3 * x + 1


s = int(input())
A = []

i = 0
while True:
    if i == 0:
        A.append(s)
    else:
        A.append(func(A[i-1]))

    i += 1

    if len(A) >= 2 and A[-1] in A[:-1]:
        break

print(len(A))