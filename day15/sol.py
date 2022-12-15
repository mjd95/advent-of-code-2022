mode = "input"

with open(mode) as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

if mode == "input":
    TARGET_ROW = 2000000
    CLAMP = 4000000
else:
    TARGET_ROW = 10
    CLAMP = 20

def get_points(line):
    parts = line.split(' ')
    sx, sy, bx, by = parts[2], parts[3], parts[8], parts[9]
    sx = sx.lstrip('x=')
    sx = int(sx.rstrip(','))
    sy = sy.lstrip('y=')
    sy = int(sy.rstrip(':'))
    bx = bx.lstrip('x=')
    bx = int(bx.rstrip(','))
    by = by.lstrip('y=')
    by = int(by)
    return (sx, sy, bx, by)

sensors = set()
beacons = set()
for line in lines:
    sx, sy, bx, by = get_points(line)
    sensors.add((sx, sy))
    beacons.add((bx, by))

def merge_intervals(intervals):
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][1]+1: 
            stack[-1][1] = max(stack[-1][1], i[1])
        else:
            stack.append(i)
    return stack

def exclusions_for_line(row):
    ints = []
    for b in beacons:
        if b[1] == row and b[0] >=0 and b[0] <= CLAMP: ints.append([b[0], b[0]])
    for s in sensors:
        if b[1] == row and s[0] >= 0 and s[0] <= CLAMP: ints.append([s[0], s[0]])
        
    for line in lines:
        sx, sy, bx, by = get_points(line)
        bdist = abs(sx-bx) + abs(sy-by)
        if abs(sy-row) > bdist:
            continue

        x_offset = bdist - abs(sy-row)
        ints.append([max(sx-x_offset, 0), min(sx+x_offset, CLAMP)])

    return merge_intervals(ints) 

#print(len(exclusions_for_line(TARGET_ROW)-beacons))

total_avail = set()
for j in range(0, CLAMP+1):
    print(f"testing row {j}")
    a = exclusions_for_line(j)
    if len(a)>1:
        x = a[0][1]+1
        print(x, j)
        print(x*4000000+j)
        break

