# https://www.acmicpc.net/problem/18766

from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    cards = list(input().split())
    test = list(input().split())
    for t in test:
        if t in cards:
            cards.remove(t)

    print("CHEATER" if cards else "NOT CHEATER")
