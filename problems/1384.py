# https://www.acmicpc.net/problem/1384

from sys import stdin

input = lambda: stdin.readline().rstrip()

T = 0
while True:
    N = int(input())
    if N == 0:
        break

    T += 1

    arr = []
    name = []
    for ii in range(N):
        paper = list(input().split())

        name.append(paper[0])
        for jj in range(1, N):
            if paper[jj] == "N":
                arr.append((ii, jj))

    print("Group", T)

    if not arr:
        print("Nobody was nasty")
        print()
        continue

    for fr, to in arr:
        print(name[fr - to], "was nasty about", name[fr])
    print()
