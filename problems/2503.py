# https://www.acmicpc.net/problem/2503

from sys import stdin
from itertools import permutations

input = lambda: stdin.readline().rstrip()

cand = list(permutations([ii for ii in range(1, 10)], 3))
N = int(input())
for _ in range(N):
    num, strike, ball = map(int, input().split())

    res = []
    for c in cand:
        st, ba = 0, 0
        for ii, check in enumerate(str(num)):
            if int(check) == c[ii]:
                st += 1
            if int(check) != c[ii] and int(check) in c:
                ba += 1

        if st == strike and ba == ball:
            res.append(c)

    cand = res

print(len(res))
