# https://www.acmicpc.net/problem/13698

from sys import stdin

input = lambda: stdin.readline().rstrip()

shuffles = {
    "A": [0, 1],
    "B": [0, 2],
    "C": [0, 3],
    "D": [1, 2],
    "E": [1, 3],
    "F": [2, 3],
}

shuffle = input()

cups = [1, 0, 0, 2]
for s in shuffle:
    ii, jj = shuffles[s]
    cups[ii], cups[jj] = cups[jj], cups[ii]

print(cups.index(1) + 1)
print(cups.index(2) + 1)
