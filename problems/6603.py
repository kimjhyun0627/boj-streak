# https://www.acmicpc.net/problem/6603

from sys import stdin
from itertools import combinations

input = stdin.readline

while True:
    set = list(map(int, input().split()))

    if len(set) == 1 and set[0] == 0:
        break

    for c in combinations(set[1:], 6):
        print(*c)

    print()
