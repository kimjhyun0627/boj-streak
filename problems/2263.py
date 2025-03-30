# https://www.acmicpc.net/problem/2263

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()


def preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    parents = postorder[post_end]
    print(parents, end=" ")

    left = position[parents] - in_start
    right = in_end - position[parents]

    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (N + 1)
for ii in range(N):
    position[inorder[ii]] = ii

preorder(0, N - 1, 0, N - 1)
