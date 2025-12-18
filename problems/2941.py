# https://www.acmicpc.net/problem/2941

from sys import stdin

input = stdin.readline

word = input().rstrip()

croatic_dict = {d: 0 for d in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]}
rem = 0

for c in croatic_dict.keys():
    croatic_dict[c] += word.count(c)
    rem += word.count(c) * len(c)

croatic_dict["z="] -= croatic_dict["dz="]
rem -= croatic_dict["dz="] * len("z=")

print(len(word) - rem + sum(croatic_dict.values()))
