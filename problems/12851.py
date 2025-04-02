# https://www.acmicpc.net/problem/12851

from sys import stdin

input = lambda: stdin.readline().rstrip()

MAX = 10**5 + 1

N, K = map(int, input().split())
visited = [-1 for _ in range(MAX)]
visited[N] = 0
queue = [N]

cnt = 0
res = 0
while queue:
    cur = queue.pop(0)

    if cnt != 0 and visited[cur] > cnt:
        continue

    if cur == K:
        cnt = visited[cur]
        res += 1
        continue

    if 0 <= cur + 1 < MAX and (
        visited[cur + 1] == -1 or visited[cur + 1] == visited[cur] + 1
    ):
        queue.append(cur + 1)
        visited[cur + 1] = visited[cur] + 1

    if 0 <= cur - 1 < MAX and (
        visited[cur - 1] == -1 or visited[cur - 1] == visited[cur] + 1
    ):
        queue.append(cur - 1)
        visited[cur - 1] = visited[cur] + 1

    if 0 <= cur * 2 < MAX and (
        visited[cur * 2] == -1 or visited[cur * 2] == visited[cur] + 1
    ):
        queue.append(cur * 2)
        visited[cur * 2] = visited[cur] + 1

print(cnt)
print(res)
