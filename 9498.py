score = int(input())

print('A' if 90 <= score <= 100 else 'B' if 80 <= score < 90 else 'C' if 70 <= score < 80 else 'D' if 60 <= score < 70 else 'F')