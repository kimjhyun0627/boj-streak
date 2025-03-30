# https://www.acmicpc.net/problem/2812
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
num = [int(n) for n in input().rstrip()]

stack = [num[0]]
removed = 0
for ii in range(1, n):
    if removed >= k:
        stack += num[ii:]
        break
    while removed < k and len(stack) and stack[-1] < num[ii]:
        stack.pop()
        removed += 1
    stack.append(num[ii])

print(*stack[: n - k], sep="")
