# https://www.acmicpc.net/problem/32403

from sys import stdin

input = stdin.readline

n, t = map(int, input().split())
lights = list(map(int, input().split()))

res = 0
for l in lights:
    num = 0
    while True:
        if (t % (l + num) == 0):
            break
        if (t % (l - num) == 0):
            break
        num += 1
    res += num
    
print(res)