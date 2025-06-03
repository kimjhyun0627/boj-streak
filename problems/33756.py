# https://www.acmicpc.net/problem/33756

from sys import stdin

input = lambda: stdin.readline().rstrip()

numbers = [int("8" * i) for i in range(18, 0, -1)]

T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0
    for num in numbers:
        while n >= num:
            n -= num
            cnt += 1

    if n == 0 and cnt <= 8:
        print("Yes")
    else:
        print("No")
