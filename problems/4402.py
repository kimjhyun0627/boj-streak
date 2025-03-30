# https://www.acmicpc.net/problem/4402

from sys import stdin

input = stdin.readline

while True:
    word = input().strip()
    if len(word) == 0:
        break
    
    prev = 0
    for w in word:
        if w in ["B", "F", "P", "V"]:
            print(1 if prev != 1 else "", end="")
            prev = 1
        elif w in ["C", "G", "J", "K", "Q", "S", "X", "Z"]:
            print(2 if prev != 2 else "", end="")
            prev = 2
        elif w in ["D", "T"]:
            print(3 if prev != 3 else "", end="")
            prev = 3
        elif w in ["L"]:
            print(4 if prev != 4 else "", end="")
            prev = 4
        elif w in ["M", "N"]:
            print(5 if prev != 5 else "", end="")
            prev = 5
        elif w in ["R"]:
            print(6 if prev != 6 else "", end="")
            prev = 6
        else:
            prev = 0
    print()
