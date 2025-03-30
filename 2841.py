# https://www.acmicpc.net/problem/2841

from sys import stdin
input = stdin.readline

n, p = map(int, input().split())

melody = [[0] for _ in range(n+1)]
count = 0
for _ in range(n):
    string, fret = map(int, input().split())
    
    if melody[string][-1] > fret:
        while melody[string][-1] > fret:
            melody[string].pop()
            count += 1
    if melody[string][-1] == fret:
        continue
    if melody[string][-1] < fret:
        melody[string].append(fret)
        count += 1
    # print(melody)
    
print(count)