# https://www.acmicpc.net/problem/4195

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def find(x):
    if x == friends[x]:
        return x

    friends[x] = find(friends[x])
    return friends[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    friends[y] = x
    sets[x] += sets[y]


T = int(input())

for _ in range(T):
    F = int(input())

    friends = dict()
    sets = dict()

    for _ in range(F):
        A, B = map(str, input().rstrip().split())
        if A not in friends:
            friends[A] = A
            sets[A] = 1
        if B not in friends:
            friends[B] = B
            sets[B] = 1

        union(A, B)
        print(sets[find(A)])
