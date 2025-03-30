# https://www.acmicpc.net/problem/30804

from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
skewer = list(map(int, input().strip().split()))

fruits = defaultdict(int)
left, right, counts = 0, 0, 0
res = 0

while right < n:
    if fruits[skewer[right]] == 0:
        counts += 1
    fruits[skewer[right]] += 1

    while counts > 2:
        fruits[skewer[left]] -= 1
        if fruits[skewer[left]] == 0:
            counts -= 1
        left += 1

    res = max(res, right - left + 1)
    right += 1

print(res)
