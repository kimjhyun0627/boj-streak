# https://www.acmicpc.net/problem/27966

n = int(input())

print((n - 1) + (n - 1) * (n - 2))
for ii in range(2, n+1):
    print(1, ii)
