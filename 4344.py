# https://www.acmicpc.net/problem/4344

from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    case = list(map(int, input().split()))
    N = case.pop(0)

    avr = sum(case) / N
    print(f"{round(len(list(filter(lambda x: x > avr, case))) / N * 100, 3):.3f}%")
