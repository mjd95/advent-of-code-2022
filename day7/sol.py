with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

class Node:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        
root = Node("/")
root.parent = None

cur = root
all_nodes = [cur]
for line in lines[1:]:
    if line[0] == "$":
        parts = line.split(" ")
        cmd = parts[1]
        if cmd == "cd":
            dr = parts[2]
            if dr == "..":
                # traverse up
                final_size = cur.size
                cur = cur.parent
                cur.size += final_size
            else:
                for c in cur.children:
                    if c.name == dr:
                        cur = c
                        break
        else:
            pass
    else:
        output = line.split(" ")
        if output[0] == "dir":
            child = Node(output[1])
            all_nodes.append(child)
            cur.add_child(child)
            child.parent = cur
        else:
            cur.size += int(output[0])

# traverse back up and fill in everything missing
while cur.parent != None:
    final_size = cur.size
    cur = cur.parent
    cur.size += final_size


tot = 0
for c in all_nodes:
    if c.size < 100000:
        tot += c.size
print(tot)

print(f"used space is {root.size}")
total_space = 70000000
unused_space = total_space - root.size
print(f"unused space is {unused_space}")
required_space = 30000000
required_free = required_space - unused_space
print(f"required free is {required_free}")
all_nodes.sort(key=lambda x: x.size)
for c in all_nodes:
    if c.size > required_free:
        print(c.size)
        break

