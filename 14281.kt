/*
# https://www.acmicpc.net/problem/14281

from sys import stdin

input = stdin.readline

n = int(input())
seq = list(map(int, input().rstrip().split()))

if len(seq) <= 2:
    print(0)
else:
    copy = seq.copy()
    ii = 1
    while ii < n - 1:
        if copy[ii] * 2 > copy[ii - 1] + copy[ii + 1]:
            copy[ii] = (copy[ii - 1] + copy[ii + 1]) // 2
            ii = ii - 1 if ii != 1 else 1
        else:
            ii += 1

    # print(copy)
    print(sum(seq) - sum(copy))
    

 */
// this python code to kotlin..

