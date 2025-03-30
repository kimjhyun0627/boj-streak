# https://www.acmicpc.net/problem/32289

from sys import stdin

n, m = map(int, stdin.readline().split())

print(
    (n - 1) * m
    + (m - 1) * n
    + 2
    * (
        (abs(m - n) + 1) * (min(m, n) - 1)
        + 2 * sum([ii for ii in range(1, min(m, n) - 1)])
    )
)
