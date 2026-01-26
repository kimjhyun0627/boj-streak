# https://www.acmicpc.net/problem/2615

from sys import stdin

input = stdin.readline

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

board = [list(map(int, input().split())) for _ in range(19)]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            focus = board[x][y]

            for ii in range(4):
                cnt = 1
                nx = x + dx[ii]
                ny = y + dy[ii]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
                    cnt += 1

                    if cnt == 5:
                        if (
                            0 <= x - dx[ii] < 19
                            and 0 <= y - dy[ii] < 19
                            and board[x - dx[ii]][y - dy[ii]] == focus
                        ):
                            break
                        if (
                            0 <= nx + dx[ii] < 19
                            and 0 <= ny + dy[ii] < 19
                            and board[nx + dx[ii]][ny + dy[ii]] == focus
                        ):
                            break
                        print(focus)
                        print(x + 1, y + 1)
                        exit(0)

                    nx += dx[ii]
                    ny += dy[ii]

print(0)
