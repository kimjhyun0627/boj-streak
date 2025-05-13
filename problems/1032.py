from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
files = [input() for _ in range(N)]

res = list(files[0])

for f in files[1:]:
    for ii in range(len(res)):
        if res[ii] != f[ii]:
            res[ii] = "?"

print("".join(res))
