with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

grid = []
for line in lines:
    row = [int(c) for c in line]
    grid.append(row)

def is_visible(grid, i, j):
    if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid)-1:
        return True

    left_visible = grid[j][i] > max([grid[j][i1] for i1 in range(0, i)])
    if left_visible: return True

    right_visible = grid[j][i] > max([grid[j][i1] for i1 in range(i+1, len(grid))])
    if right_visible: return True

    top_visible = grid[j][i] > max([grid[j1][i] for j1 in range(0, j)])
    if top_visible: return True

    bottom_visible = grid[j][i] > max([grid[j1][i] for j1 in range(j+1, len(grid))])
    if bottom_visible: return True

    return False
            
tot = 0
for j in range(0, len(grid)):
    for i in range(0, len(grid)):
        if is_visible(grid, i, j):        
            tot += 1
print(tot)

def calculate_score(grid, i, j):
    j1 = 1
    while j-j1 >= 0:
        if grid[j][i] <= grid[j-j1][i]:
            j1 += 1
            break
        else:
            j1 += 1
    top_score = j1-1

    i1 = 1
    while i-i1 >= 0:
        if grid[j][i] <= grid[j][i-i1]:
            i1 += 1
            break
        else:
            i1 += 1
    left_score = i1-1

    i1 = 1
    while i+i1 < len(grid):
        if grid[j][i] <= grid[j][i+i1]:
            i1 += 1
            break
        else:
            i1 += 1
    right_score = i1-1


    j1 = 1
    while j+j1 < len(grid):
        if grid[j][i] <= grid[j+j1][i]:
            j1 += 1
            break
        else: 
            j1 += 1
    bottom_score = j1-1

    return left_score * right_score * top_score * bottom_score
    

scores = []
for j in range(0, len(grid)):
    row = []
    for i in range(0, len(grid)):
        score = calculate_score(grid, i, j)
        row.append(score)
    scores.append(row)
mx = -1
for j in range(len(scores)):
    mx = max(mx, max(scores[j]))
print(mx)
