with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

cycle = 0
register = 1
ss = 0

def add_ss(ss, cycle, register):
    if cycle%40==20:
        ss += cycle*register
    return ss

for line in lines:
    if line == "noop":
        cycle += 1
        ss = add_ss(ss, cycle, register)
    else:
        (op, val) = line.split(" ")
        cycle += 1
        ss = add_ss(ss, cycle, register)
        cycle += 1
        ss = add_ss(ss, cycle, register)
        register += int(val) 


cycle = 0
register = 1
grid = [['.']*40 for j in range(6)]
def print_grid(grid):
    for j in range(len(grid)):
        print(''.join(grid[j]))

def color_pixel(register, cycle):
    pos = cycle-1
    i = pos%40
    j = pos//40
    if i == register-1 or i == register or i == register+1:
        grid[j][i] = '#'  

for line in lines:
    if line == "noop":
        cycle += 1
        color_pixel(register, cycle)
    else:
        (op, val) = line.split(" ")
        cycle += 1
        color_pixel(register, cycle)
        cycle += 1
        color_pixel(register, cycle)
        register += int(val) 

print_grid(grid)
