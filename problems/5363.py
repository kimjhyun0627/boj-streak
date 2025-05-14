# https://www.acmicpc.net/problem/5363

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    sentence = list(map(str, input().split()))
    print(*sentence[2:], *sentence[:2])
