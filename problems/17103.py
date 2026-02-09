# https://www.acmicpc.net/problem/17103

from sys import stdin

input = stdin.readline


prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for ii in range(2, 1000001):
    if check[ii] == 0:
        prime.append(ii)
        for jj in range(2 * ii, 1000001, ii):
            check[jj] = 1

T = int(input())

for _ in range(T):
    count = 0
    N = int(input().rstrip())
    for ii in prime:
        if ii >= N:
            break
        if not check[N - ii] and ii <= N - ii:
            count += 1
    print(count)
