# https://www.acmicpc.net/problem/1918

infix = input()
stack = []

for i in infix:
    if i.isalpha():
        print(i, end="")
    if i == "(":
        stack.append(i)
    if i == ")":
        while stack and stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop()
    if i in ["*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            print(stack.pop(), end="")
        stack.append(i)
    if i in ["+", "-"]:
        while stack and stack[-1] in ["*", "/", "+", "-"]:
            print(stack.pop(), end="")
        stack.append(i)

while stack:
    print(stack.pop(), end="")
