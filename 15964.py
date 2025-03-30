# https://www.acmicpc.net/problem/15964

from sys import stdin

input = lambda: stdin.readline().rstrip()

A, B = map(int, input().split())

print((A + B) * (A - B))
