import math

N = int(input())
notax = math.ceil(N / 1.08)
if N == math.floor(notax * 1.08):
    print(notax)
else:
    print(':(')