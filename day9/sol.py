with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

def move(dr, pt):
    if dr == "R":
        pt = (pt[0]+1, pt[1])
    elif dr == "U":
        pt = (pt[0], pt[1]+1)
    elif dr == "L":
        pt = (pt[0]-1, pt[1])
    elif dr == "D":
        pt = (pt[0], pt[1]-1)
    else:
        print("borked")
    return pt

def catchup(t, h):
    # check if move is necessary
    valid_pos = [(h[0]+dx, h[1]+dy) for (dx, dy) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]]
    if t in valid_pos:
        return t

    # check axes moves
    if t[0] == h[0]:
        if h[1] > t[1]:
            return (t[0], t[1]+1)
        else:
            return (t[0], t[1]-1)
    if t[1] == h[1]:
        if h[0] > t[0]:
            return (t[0]+1, t[1])
        else:
            return (t[0]-1, t[1])

    # check diagonal moves
    for (dx, dy) in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        if (t[0]+dx, t[1]+dy) in valid_pos:
            return (t[0]+dx, t[1]+dy)

    print("borked")

rope = []
for i in range(10):
    rope.append((0, 0))
seen = set()
for line in lines:
    (dr, amt) = line.split(" ")
    amt = int(amt)

    while amt > 0:
        rope[0] = move(dr, rope[0])
        amt -= 1 
        for i in range(1, 10):
            rope[i] = catchup(rope[i], rope[i-1])
        seen.add(rope[-1])
print(len(seen))
