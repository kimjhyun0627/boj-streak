# https://www.acmicpc.net/problem/11501

from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    ans = 0
    for ii in range(len(price) - 1, -1, -1):
        if price[ii] > max_price:
            max_price = price[ii]
        else:
            ans += max_price - price[ii]
    print(ans)
