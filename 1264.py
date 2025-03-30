# https://www.acmicpc.net/problem/1264

from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    sentence = input()
    if sentence == "#":
        break
    print(sum([sentence.lower().count(v) for v in ["a", "e", "i", "o", "u"]]))
