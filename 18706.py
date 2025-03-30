# https://www.acmicpc.net/problem/18706

from sys import stdin
from collections import defaultdict

input = stdin.readline

SMALL = 0
MEDIUM = 1
LARGE = 2

t = int(input())

for _ in range(t):
    c, p = map(int, input().rstrip().split())
    menu = {}
    for _ in range(c):
        coffee, s, m, l = input().rstrip().split()
        menu[coffee] = [int(x) for x in [s, m, l]]

    payment = defaultdict(int)
    for _ in range(p):
        name, size, order = input().rstrip().split()
        if size == "small":
            payment[name] += menu[order][SMALL]
        if size == "medium":
            payment[name] += menu[order][MEDIUM]
        if size == "large":
            payment[name] += menu[order][LARGE]

    delivery = 100 // len(payment)
    for c in payment:
        payment[c] += delivery
        if payment[c] % 5 == 1:
            payment[c] -= 1
        if payment[c] % 5 == 4:
            payment[c] += 1

    for p in payment:
        print(p, payment[p])
