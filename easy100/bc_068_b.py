N = int(input())
bin_n = bin(N)[2:]
if bin_n == '1':
    print(1)
else:
    ans = bin_n[0] + bin_n[1:].replace('1', '0')
    print(int(ans, 2))