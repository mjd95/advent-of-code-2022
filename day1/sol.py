with open("input") as f:
    lines = [l.strip() for l in f.readlines()]

cals = []
cur = 0
for line in lines:
    if line != "":
        cur += int(line)
    else:
        cals.append(cur)
        cur = 0
cals.append(cur)

print(max(cals))

m1 = max(cals)
cals.remove(m1)

m2 = max(cals)
cals.remove(m2)

m3 = max(cals)
print(m1+m2+m3)
