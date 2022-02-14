S = input()
atcg = ['A', 'T', 'G', 'C']

count = 0
count_max = 0
for s in list(S):
    if s in atcg:
        count += 1
        if count_max < count:
            count_max = count
    else:
        count = 0

print(count_max)
