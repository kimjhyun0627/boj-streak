# https://www.acmicpc.net/problem/6438

from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    print(input().rstrip()[::-1])