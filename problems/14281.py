# https://www.acmicpc.net/problem/14281

from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

if len(arr) <= 2:
    print(0)
else:
    seq = arr.copy()
    while True:
        convex = True
        
        for ii in range(1, n-1):
            if seq[ii] * 2 > seq[ii - 1] + seq[ii + 1]:
                seq[ii] = (seq[ii - 1] + seq[ii + 1]) // 2
                convex = False
        
        if convex:
            break
        
    print(sum(arr) - sum(seq))
