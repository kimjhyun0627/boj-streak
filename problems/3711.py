# https://www.acmicpc.net/problem/3711

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    nums = []
    G = int(input())
    for _ in range(G):
        nums.append(int(input()))

    for ii in range(1, 10**6):
        mods = []
        valid = True
        for n in nums:
            if n % ii in mods:
                valid = False
                break
            mods.append(n % ii)
        if valid:
            print(ii)
            break
