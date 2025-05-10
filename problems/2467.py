# https://www.acmicpc.net/problem/2467

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
liqs = list(map(int, input().split()))

left, right = 0, 0
diff = float("inf")

for ii in range(N - 1):
    target = liqs[ii]
    start, end = ii + 1, N - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = target + liqs[mid]

        if abs(tmp) < diff:
            diff = abs(tmp)
            left = ii
            right = mid
            if tmp == 0:
                break

        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(liqs[left], liqs[right])
