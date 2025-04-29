# https://www.acmicpc.net/problem/5554

from sys import stdin

input = lambda: stdin.readline().rstrip()

time = sum([int(input()) for _ in range(4)])

print(time // 60)
print(time % 60)
