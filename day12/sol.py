from collections import defaultdict

with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

grid = [[c for c in line] for line in lines]


def get_nbrs(cur, grid):
    x, y = cur[0], cur[1]
    cands = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    cands1 = filter(lambda p: p[0]>=0 and p[0]<len(grid[0]) and p[1]>=0 and p[1]<len(grid), cands)
    cands2 = filter(lambda p: ord(grid[p[1]][p[0]]) <= ord(grid[cur[1]][cur[0]])+1, cands1)
    return cands2

def get_next(distances, visited):
    nxt = None
    min_d = 1000000
    for (p, d) in distances.items():
        if p not in visited and d < min_d:
            nxt = p
            min_d = d
    return nxt 

possible_starts = []
for j in range(len(grid)):
    for i in range(len(grid[j])):
        if grid[j][i] == 'S':
            start = (i, j)
            grid[j][i] = 'a'
        if grid[j][i] == 'E':
            end = (i, j)
            grid[j][i] = 'z'
        if grid[j][i] == 'a':
            possible_starts.append((i, j))

def find_best(start):
    visited = set()
    distances = defaultdict(lambda: 10e12)

    distances[(start[0], start[1])] = 0
    cur = (start[0], start[1])
    while cur != None:
        for nbr in get_nbrs(cur, grid):
            if nbr not in visited:
                distances[nbr] = min(distances[nbr], 1+distances[cur])
        visited.add(cur)
        if end in visited:
            break
        cur = get_next(distances, visited)
    return distances

print(find_best(start)[end])

print(min([find_best(s)[end] for s in possible_starts]))
