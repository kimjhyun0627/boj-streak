# https://www.acmicpc.net/problem/2480

from sys import stdin
from collections import Counter

input = lambda: stdin.readline().rstrip()

nums = Counter(map(int, input().split()))

if len(nums) == 1:
    print(10000 + nums.most_common(1)[0][0] * 1000)
if len(nums) == 2:
    print(1000 + nums.most_common(1)[0][0] * 100)
if len(nums) == 3:
    print(max(nums) * 100)
