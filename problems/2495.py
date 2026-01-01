# https://www.acmicpc.net/problem/2495

from sys import stdin

input = stdin.readline

for _ in range(3):
    digit = input().rstrip()

    ans = 1
    prev = -1
    cnt = 1

    for d in digit:
        # print(d, prev, cnt)
        if int(d) == prev:
            cnt += 1
        else:
            prev = int(d)
            cnt = 1

        ans = max(ans, cnt)

    print(ans)
