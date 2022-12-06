filename = "input"

with open(filename) as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

if filename == "test":
    stacks = [[], ['Z', 'N'], ['M', 'C', 'D'], ['P']]
elif filename == "input":
    stacks = [
      [],
      ["Z", "J", "N", "W", "P", "S"],
      ["G", "S", "T"],
      ["V", "Q", "R", "L", "H"],
      ["V", "S", "T", "D"],
      ["Q", "Z", "T", "D", "B", "M", "J"],
      ["M", "W", "T", "J", "D", "C", "Z", "L"],
      ["L", "P", "M", "W", "G", "T", "J"],
      ["N", "G", "M", "T", "B", "F", "Q", "H"],
      ["R", "D", "G", "C", "P", "B", "Q", "W"]
    ]

def parse_line(line):
    parts = line.split(' ')
    amt = int(parts[1])
    src = int(parts[3])
    dst = int(parts[5])
    return (amt, src, dst)

for line in lines:
    if line[0] != 'm':
        continue
    (amt, src, dst) = parse_line(line)
    while amt > 0:
        tmp = stacks[src].pop()
        stacks[dst].append(tmp)
        amt -= 1

print(''.join([s[-1] for s in stacks[1:]]))

if filename == "test":
    stacks = [[], ['Z', 'N'], ['M', 'C', 'D'], ['P']]
elif filename == "input":
    stacks = [
      [],
      ["Z", "J", "N", "W", "P", "S"],
      ["G", "S", "T"],
      ["V", "Q", "R", "L", "H"],
      ["V", "S", "T", "D"],
      ["Q", "Z", "T", "D", "B", "M", "J"],
      ["M", "W", "T", "J", "D", "C", "Z", "L"],
      ["L", "P", "M", "W", "G", "T", "J"],
      ["N", "G", "M", "T", "B", "F", "Q", "H"],
      ["R", "D", "G", "C", "P", "B", "Q", "W"]
    ]


for line in lines:
    if line[0] != 'm':
        continue
    (amt, src, dst) = parse_line(line)
    tmp = stacks[src][-amt:]
    stacks[src] = stacks[src][:-amt]
    stacks[dst] = stacks[dst] + tmp

print(''.join([s[-1] for s in stacks[1:]]))
