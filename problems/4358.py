# https://www.acmicpc.net/problem/4358

from sys import stdin
from collections import defaultdict

input = lambda: stdin.readline().rstrip()

species = defaultdict(int)
while True:
    tree = input().rstrip()
    if tree == "":
        break
    species[tree] += 1

size = sum(species.values())
res = sorted(species.keys())

for r in res:
    if r == "":
        break
    num = (species[r] / size) * 100
    print(r, format(num, ".4f"))
