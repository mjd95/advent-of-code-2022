from collections import defaultdict

mode = "input"

shapes = [[['#', '#', '#', '#']], [['.', '#', '.'], ['#', '#' , '#'], ['.', '#', '.']], [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']], [['#'], ['#'], ['#'], ['#']], [['#', '#'], ['#', '#']]]

with open(mode) as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

stream = lines[0]
grid_height = 100000

class Sim:
    def __init__(self, stream):
        self.stream = stream
        self.grid = [['.' for i in range(7)] for j in range(grid_height)]
        self.start_height = 3
        self.stream_idx = 0
        self.seen = {}

    def print_grid(self, h):
        for j in range(h-1, -1, -1):
            print(''.join(self.grid[j]))
        print("---")


    def is_terminal_pos(self, shape, i, j):
        for j1 in range(len(shape)):
            for i1 in range(len(shape[j1])):
                if shape[j1][i1] == '#':
                    if j+j1 == 0 or self.grid[j+j1-1][i+i1] == '#':
                        return True
        return False

    def draw_shape(self, shape, i, j):
        for j1 in range(len(shape)):
            for i1 in range(len(shape[j1])):
                if shape[j1][i1] == '#':
                    self.grid[j+j1][i+i1] = '#'

    def apply_stream(self, shape, i, j):
        dr = self.stream[self.stream_idx%len(self.stream)]
        self.stream_idx += 1
        if dr == '>':
            # check if can move right
            for j1 in range(len(shape)):
                for i1 in range(len(shape[j1])):
                    if shape[j1][i1] == '#':
                        # if we have a rock on the right boundary, certainly can't move any further right
                        if i+i1 == len(self.grid[j1])-1:
                            return i
                        # if we're not on the right boundary but there's a rock to a right, also can't
                        if self.grid[j+j1][i+i1+1] == '#':
                            return i
            return i+1
        else:
            # check if can move left
            for j1 in range(len(shape)):
                for i1 in range(len(shape[j1])):
                    if shape[j1][i1] == '#':
                        if i+i1 == 0:
                            return i
                        if self.grid[j+j1][i+i1-1] == '#':
                            return i
            return i-1
            
    def get_input_state(self, op):
        shape_idx = op%len(shapes)
        stream_idx = self.stream_idx%len(self.stream)
        ts = []
        for i in range(7):
            t = 0
            while True:
                if self.start_height-t == 0 or self.grid[self.start_height-t-1][i] == '#':
                    ts.append(t)
                    break
                else:
                    t += 1
        return (shape_idx, stream_idx, tuple(ts))

    def drop_shape(self, shape_idx):
        shape = shapes[shape_idx%len(shapes)]
        i = 2
        j = self.start_height
        while True:
            i = self.apply_stream(shape, i, j)
            if self.is_terminal_pos(shape, i, j):
                self.draw_shape(shape, i, j)
                break
            else:
                j -= 1
        self.start_height = max(self.start_height, j + len(shape) + 3)

    def run(self, amt):
        t = 0
        cycle_h = 0
        cycled = False
        while t < amt:
            state = self.get_input_state(t)
            if state in self.seen and not cycled:
                prvt, prvh = self.seen[state]
                hdiff = self.start_height-3 - prvh
                tdiff = t - prvt
                print(f"cycle length is {tdiff}")
                repeats = (amt-t)//tdiff
                t += repeats * tdiff
                print(f"fast forwarded to {t}")
                print(f"remaining is {amt-t}")
                cycle_h = repeats * hdiff
                cycled = True
            else:
                self.seen[state] = (t, self.start_height-3)
                self.drop_shape(t)
                t += 1

        print(f"final height {self.start_height-3+cycle_h}")

sim = Sim(stream)
sim.run(1000000000000)
