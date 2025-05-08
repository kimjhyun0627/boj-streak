# https://www.acmicpc.net/problem/1985

from sys import stdin

input = lambda: stdin.readline().rstrip()


def is_friends(x: str, y: str) -> bool:
    flag1 = [False] * 10
    flag2 = [False] * 10

    for ch in x:
        flag1[int(ch)] = True
    for ch in y:
        flag2[int(ch)] = True

    return flag1 == flag2


def fix_numbers(x: str, y: str) -> bool:
    x = list(x)
    for i in range(len(x) - 1):
        original_x = x[:]

        # Try decrease x[i] and increase x[i+1]
        if x[i] > "0" and x[i + 1] < "9":
            x[i] = str(int(x[i]) - 1)
            x[i + 1] = str(int(x[i + 1]) + 1)
            if is_friends("".join(x), y) and x[0] != "0":
                print("almost friends")
                return True
            x = original_x[:]

        # Try increase x[i] and decrease x[i+1]
        if x[i] < "9" and x[i + 1] > "0":
            x[i] = str(int(x[i]) + 1)
            x[i + 1] = str(int(x[i + 1]) - 1)
            if is_friends("".join(x), y) and x[0] != "0":
                print("almost friends")
                return True
            x = original_x[:]

    return False


def main():
    for _ in range(3):
        x, y = input().strip().split()

        if is_friends(x, y):
            print("friends")
            continue

        if fix_numbers(x, y):
            continue
        if fix_numbers(y, x):
            continue

        print("nothing")


if __name__ == "__main__":
    main()
