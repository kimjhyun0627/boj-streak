# https://www.acmicpc.net/problem/9019

from sys import stdin
from collections import deque

input = stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().strip().split())

    queue = deque()
    queue.append([a, ""])
    check = [False] * 10001

    while queue:
        h, c = queue.popleft()

        if h == b:
            print(c)
            break

        d = 2 * h % 10000
        if not check[d]:
            queue.append([d, c + "D"])
            check[d] = True

        s = h - 1 if h else 9999
        if not check[s]:
            queue.append([s, c + "S"])
            check[s] = True

        l = (h * 10) % 10000 + (h // 1000)
        if not check[l]:
            queue.append([l, c + "L"])
            check[l] = True

        r = (h // 10) + (h % 10) * 1000
        if not check[r]:
            queue.append([r, c + "R"])
            check[r] = True
