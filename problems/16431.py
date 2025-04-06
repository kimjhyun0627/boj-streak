bx, by = map(int, input().split())
dx, dy = map(int, input().split())
jx, jy = map(int, input().split())

bessie = max(abs(jx - bx), abs(jy - by))
daisy = abs(jx - dx) + abs(jy - dy)

print("bessie" if bessie < daisy else "daisy" if bessie > daisy else "tie")
