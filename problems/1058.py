# https://www.acmicpc.net/problem/1058

from sys import stdin

input = stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

friends = [[[], []] for _ in graph]

for ii in range(n):
    for jj in range(n):
        if graph[ii][jj] == "Y":
            friends[ii][0].append(jj)

for ii in range(n):
    for jj in range(n):
        if graph[ii][jj] == "Y":
            friends[ii][1] += friends[jj][0]

    friends[ii][1] = list(set(friends[ii][1]))
    if ii in friends[ii][1]:
        friends[ii][1].remove(ii)

print(len(max([set(f[0] + f[1]) for f in friends], key=len)))
