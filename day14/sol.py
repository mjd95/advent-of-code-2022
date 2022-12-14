def print_grid(grid, width):
    for j in range(max_h+3):
        print(''.join(grid[j][500-width:500+width+1]))

def get_dr(c, n):
    if c[0] == n[0]:
        if n[1] > c[1]: return (0, 1)
        elif n[1] < c[1]: return (0, -1)
        else: print(f"ERROR1 {n} {c}")
    elif c[1] == n[1]:
        if n[0] > c[0]: return (1, 0)
        elif n[0] < c[0]: return (-1, 0)
        else: print("ERROR2")
    else:
        print("ERROR3")

with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

max_h = 0
segments = []
for line in lines:
    parts = line.split(' -> ')
    segment = []
    for part in parts:
        x = part.split(',')
        segment.append((int(x[0]), int(x[1])))
        max_h = max(int(x[1]), max_h)
        
    segments.append(segment)

grid = [['.' for i in range(1000)] for j in range(max_h+2)]
grid.append(['#' for i in range(1000)])

# draw segments
for s in segments:
    for i in range(0, len(s)-1):
        cur = s[i]
        dr = get_dr(cur, s[i+1])
        while cur != s[i+1]:
            grid[cur[1]][cur[0]] = '#'
            cur = (cur[0]+dr[0], cur[1]+dr[1])
            grid[cur[1]][cur[0]] = '#'

print_grid(grid, 10)
print("-----")
    
should_continue = True
dropped = 0
while True:
    if not should_continue:
        break

    p = (500, 0)
    dropped += 1
    while True:
        if grid[p[1]+1][p[0]] == '.':
            p = (p[0], p[1]+1)
        elif grid[p[1]+1][p[0]-1] == '.':
            p = (p[0]-1, p[1]+1)
        elif grid[p[1]+1][p[0]+1] == '.':
            p = (p[0]+1, p[1]+1)
        else:
            # can't move any futher
            if p == (500, 0):
                should_continue = False
            grid[p[1]][p[0]] = 'o'
            break
print_grid(grid, 10)
 
print(dropped)
