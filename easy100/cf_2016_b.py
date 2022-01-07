N, A, B = map(int, input().split())
S = input()

pass_c = 0
b_rank = 1
for i in range(N):
    if S[i] == 'a' and pass_c < A + B:
        print('Yes')
        pass_c += 1
    elif S[i] == 'b' and pass_c < A + B and b_rank <= B:
        print('Yes')
        pass_c += 1
        b_rank += 1
    else:
        print('No')