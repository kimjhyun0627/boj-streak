# https://www.acmicpc.net/problem/1469

from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**7)

n = int(input())
sets = sorted(list(map(int, input().split())))

s = [-1 for _ in range(n * 2)]
visited = [False for _ in range(17)]


def dfs(index):

    if index == n * 2:
        for i in s:
            print(i, end=" ")
        exit(0)

    if s[index] != -1:
        dfs(index + 1)
        return

    for i in range(n):
        num = sets[i]
        next_index = index + num + 1
        if not visited[num]:
            if 0 <= next_index < n * 2 and s[next_index] == -1:
                s[index] = num
                s[next_index] = num
                visited[num] = True
                dfs(index + 1)
                s[index] = -1
                s[next_index] = -1
                visited[num] = False


dfs(0)

print(-1)
