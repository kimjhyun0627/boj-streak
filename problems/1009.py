# https://www.acmicpc.net/problem/1009

from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    cycle = []
    current = a % 10

    while current not in cycle:
        cycle.append(current)
        current = (current * a) % 10

    index = (b - 1) % len(cycle)
    result = cycle[index]

    print(10 if result == 0 else result)
