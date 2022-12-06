from collections import defaultdict

with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

def prio(c):
    if c.islower():
        return ord(c)-96
    else:
        return prio(c.lower()) + 26

tot = 0
for line in lines:
    mid = len(line)//2
    left = line[:mid]
    right = line[mid:]
    for c in right:
        if c in left:
            tot += prio(c)
            break
print(tot)

tot = 0
for i in range(0, len(lines)//3):
    counts = defaultdict(int) 
    for c in set(lines[3*i]):
        counts[c] += 1
    for c in set(lines[3*i+1]):
        counts[c] += 1
    for c in set(lines[3*i+2]):
        if counts[c] == 2:
            tot += prio(c)
            break
print(tot)
