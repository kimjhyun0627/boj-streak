# https://www.acmicpc.net/problem/26086

from sys import stdin
from collections import deque

input = stdin.readline

N, Q, k = map(int, input().split())

commands = [tuple(map(int, input().split())) for _ in range(Q)]
srt = max([ii if command[0] == 1 else 0 for ii, command in enumerate(commands)])
dq = deque([command[1] for command in commands[:srt] if command[0] == 0])
rev = sum([command[0] == 2 for command in commands[:srt]])%2 == 1

if srt != 0:
    dq = deque(sorted(dq))
    rev = False

for command in commands[srt:]:
    if command[0] == 0:
        dq.append(command[1]) if rev else dq.appendleft(command[1])
    elif command[0] == 2:
        rev = not rev

# print(dq)
print(dq[-k] if rev else dq[k-1])