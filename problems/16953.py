# https://www.acmicpc.net/problem/16953

from sys import stdin
from collections import deque

input = stdin.readline

A, B = map(int, input().split())

queue = deque([(A, 1)])
res = -1
while queue:
    cur, cnt = queue.popleft()
    if cur == B:
        res = cnt
        break
    if cur * 2 <= B:
        queue.append((cur * 2, cnt + 1))
    if cur * 10 + 1 <= B:
        queue.append((cur * 10 + 1, cnt + 1))

print(res)
