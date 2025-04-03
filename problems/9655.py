# https://www.acmicpc.net/problem/9655

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

print("SK" if N % 2 else "CY")
