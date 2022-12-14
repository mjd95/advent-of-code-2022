import functools
import copy

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

def has_nested(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            return True
    return False

def compare(left_orig, right_orig):
    left = copy.deepcopy(left_orig)
    right = copy.deepcopy(right_orig) 
    # check if there are no nested lists involved, then it is easy
    for i in range(min(len(left), len(right))):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
        else:
            if isinstance(left[i], int):
                left[i] = [left[i]]
            elif isinstance(right[i], int):
                right[i] = [right[i]]
            sub = compare(left[i], right[i])
            if sub is not None:
                return sub
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

def cmp(left, right):
    if compare(left, right):
        return 1
    else:
        return -1
    
tot = 0
all_packets = []
for i in range(len(lines)//3+1):
    left = eval(lines[3*i])
    right = eval(lines[3*i+1])
    all_packets.append(left)
    all_packets.append(right)
    in_order = compare(left, right)
    if in_order:
        tot += (i+1)

print(tot)

all_packets.append([[2]])
all_packets.append([[6]])
srt = sorted(all_packets, key=functools.cmp_to_key(cmp), reverse=True)
ans = 1
for i, s in enumerate(srt):
    if s == [[2]] or s==[[6]]:
       ans *= (i+1) 
print(ans)
