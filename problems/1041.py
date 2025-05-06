# https://www.acmicpc.net/problem/1041

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(sum(sorted(nums)[:5]))
else:
    mins = sorted([min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])])
    print(
        ((N - 2) ** 2 + (N - 1) * (N - 2) * 4) * mins[0]
        + ((N - 1) * 4 + (N - 2) * 4) * (mins[0] + mins[1])
        + 4 * (mins[0] + mins[1] + mins[2])
    )
