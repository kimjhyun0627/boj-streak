# https://www.acmicpc.net/problem/14370

from collections import Counter
from sys import stdin

input = stdin.readline

N = int(input())
cases = [dict(Counter(input().rstrip())) for _ in range(N)]

for idx, case in enumerate(cases, start=1):
    ans = []
    while 'Z' in case and case['Z'] > 0:
        ans.append(0)
        case['Z'] -= 1
        case['E'] -= 1
        case['R'] -= 1
        case['O'] -= 1
    while 'W' in case and case['W'] > 0:
        ans.append(2)
        case['T'] -= 1
        case['W'] -= 1
        case['O'] -= 1
    while 'U' in case and case['U'] > 0:
        ans.append(4)
        case['F'] -= 1
        case['O'] -= 1
        case['U'] -= 1
        case['R'] -= 1
    while 'X' in case and case['X'] > 0:
        ans.append(6)
        case['S'] -= 1
        case['I'] -= 1
        case['X'] -= 1
    while 'G' in case and case['G'] > 0:
        ans.append(8)
        case['E'] -= 1
        case['I'] -= 1
        case['G'] -= 1
        case['H'] -= 1
        case['T'] -= 1
    while 'O' in case and case['O'] > 0:
        ans.append(1)
        case['O'] -= 1
        case['N'] -= 1
        case['E'] -= 1
    while 'H' in case and case['H'] > 0:
        ans.append(3)
        case['T'] -= 1
        case['H'] -= 1
        case['R'] -= 1
        case['E'] -= 2
    while 'F' in case and case['F'] > 0:
        ans.append(5)
        case['F'] -= 1
        case['I'] -= 1
        case['V'] -= 1
        case['E'] -= 1
    while 'S' in case and case['S'] > 0:
        ans.append(7)
        case['S'] -= 1
        case['E'] -= 2
        case['V'] -= 1
        case['N'] -= 1
    while 'I' in case and case['I'] > 0:
        ans.append(9)
        case['N'] -= 2
        case['I'] -= 1
        case['E'] -= 1

    print(f'Case #{idx}: ', *sorted(ans), sep='')