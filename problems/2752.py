# https://www.acmicpc.net/problem/2752

from sys import stdin

input = lambda: stdin.readline().rstrip()

print(*sorted(list(map(int, input().split()))))
