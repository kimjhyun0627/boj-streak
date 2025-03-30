s = input()

counts = []
for ii in range(26):
    counts.append(s.find(chr(97+ii)))

print(' '.join(map(str, counts)))