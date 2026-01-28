# https://www.acmicpc.net/problem/12852

from sys import stdin

input = stdin.readline

N = int(input())

graph = [ii - 1 for ii in range(N + 1)]
operation = [int(1e9) for _ in range(N + 1)]
operation[1] = 0

for ii in range(2, N + 1):
    operation[ii] = operation[ii - 1] + 1
    if ii % 2 == 0 and operation[ii // 2] + 1 < operation[ii]:
        graph[ii] = ii // 2
        operation[ii] = operation[ii // 2] + 1
    if ii % 3 == 0 and operation[ii // 3] + 1 < operation[ii]:
        graph[ii] = ii // 3
        operation[ii] = operation[ii // 3] + 1

ans = [N]
cur = N
while cur != 1:
    ans.append(graph[cur])
    cur = graph[cur]

print(operation[N])
print(*ans)
