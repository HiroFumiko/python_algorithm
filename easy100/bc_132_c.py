N = int(input())
D = list(map(int, input().split()))

D.sort()
min_num = D[:int(N/2)][-1]
max_num = D[int(-N/2):][0]

print(max_num - min_num)