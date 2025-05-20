# https://www.acmicpc.net/problem/1021

from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))
count = 0

for target in targets:
    idx = dq.index(target)
    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        count += idx
    else:
        dq.rotate(len(dq) - idx)
        count += len(dq) - idx
    dq.popleft()

print(count)
