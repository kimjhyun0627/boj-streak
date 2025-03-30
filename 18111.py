# https://www.acmicpc.net/problem/18111

from sys import stdin

input = stdin.readline

n, m, b = map(int, input().rstrip().split())
ground = [list(map(int, input().rstrip().split())) for _ in range(n)]

time = 64000000*2+1
level = -1

for ii in range(0, 257):
    puts = 0
    removes = 0
    inventory = b

    for jj in range(n):
        for kk in range(m):
            cost = ground[jj][kk] - ii
            if cost < 0:
                puts += -cost
                inventory += cost
            if cost > 0:
                removes += cost * 2
                inventory += cost
    if inventory >= 0 and removes + puts <= time:
        time = removes + puts
        res = ii
        
print(time, res)
