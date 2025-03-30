# https://www.acmicpc.net/problem/17504

from sys import stdin, setrecursionlimit
from math import gcd

input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

arr = list(map(int, input().split()))


def rec(idx):
    if idx == len(arr) - 1:
        return (1, arr[idx])
    nu, de = rec(idx + 1)
    tmp = arr[idx] * de + nu
    return (
        (de, tmp)
        if idx != 0
        else (tmp - de // gcd(tmp - de, tmp), tmp // gcd(tmp - de, tmp))
    )


print(*rec(0))
