# https://www.acmicpc.net/problem/2530

from sys import stdin

input = lambda: stdin.readline().rstrip()

H, M, S = map(int, input().split())

res = (H * 60 * 60 + M * 60 + S + int(input())) % (24 * 60 * 60)
print(res // (60 * 60), (res // 60) % 60, res % 60)
