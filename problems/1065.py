# https://www.acmicpc.net/problem/1065

from sys import stdin

input = lambda: stdin.readline().rstrip()


def han(n):
    count = 0
    for ii in range(100, n + 1):
        tmp = list(map(int, str(ii)))
        diff = [tmp[idx] - tmp[idx - 1] for idx in range(1, len(tmp))]
        count += int(len(set(diff)) == 1)
    return min(n, count + 99)


N = int(input())

print(han(N))
