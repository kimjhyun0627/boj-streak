# https://www.acmicpc.net/problem/4101

from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    print("Yes" if n > m else "No")
