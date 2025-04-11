# https://www.acmicpc.net/problem/2083

from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    name, age, weight = input().split()
    if name == "#" and not int(age) and not int(weight):
        break

    print(name, "Junior" if int(age) <= 17 and int(weight) < 80 else "Senior")
