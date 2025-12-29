# https://www.acmicpc.net/problem/12789

from sys import stdin

input = stdin.readline

N = int(input())
tickets = list(map(int, input().split()))

queue = []
next = 1
for t in tickets:
    # print("q:", queue)
    if t == next:
        next += 1
    else:
        queue.append(t)

    while queue and queue[-1] == next:
        queue.pop()
        next += 1

print("Sad" if queue else "Nice")
