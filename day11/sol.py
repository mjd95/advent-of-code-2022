class Monkey:
    def __init__(self, items, op, mod, true_dest, false_dest):
        self.items = items
        self.op = op
        self.mod = mod 
        self.true_dest = true_dest
        self.false_dest = false_dest

##test input
#
#monkeys = []
#
##Monkey 0:
##  Starting items: 79, 98
##  Operation: new = old * 19
##  Test: divisible by 23
##    If true: throw to monkey 2
##    If false: throw to monkey 3
#
#monkeys.append(Monkey([79, 98], lambda x: x*19, 23, 2, 3))
#
##Monkey 1:
##  Starting items: 54, 65, 75, 74
##  Operation: new = old + 6
##  Test: divisible by 19
##    If true: throw to monkey 2
##    If false: throw to monkey 0
#
#monkeys.append(Monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0))
#
##Monkey 2:
##  Starting items: 79, 60, 97
##  Operation: new = old * old
##  Test: divisible by 13
##    If true: throw to monkey 1
##    If false: throw to monkey 3
#
#monkeys.append(Monkey([79, 60, 97], lambda x: x*x, 13, 1, 3))
#
##Monkey 3:
##  Starting items: 74
##  Operation: new = old + 3
##  Test: divisible by 17
##    If true: throw to monkey 0
##    If false: throw to monkey 1
#
#monkeys.append(Monkey([74], lambda x: x+3, 17, 0, 1))

#real input

monkeys = []

#Monkey 0:
#  Starting items: 59, 74, 65, 86
#  Operation: new = old * 19
#  Test: divisible by 7
#    If true: throw to monkey 6
#    If false: throw to monkey 2

monkeys.append(Monkey([59, 74, 65, 86], lambda x: x*19, 7, 6, 2))

#Monkey 1:
#  Starting items: 62, 84, 72, 91, 68, 78, 51
#  Operation: new = old + 1
#  Test: divisible by 2
#    If true: throw to monkey 2
#    If false: throw to monkey 0

monkeys.append(Monkey([62, 84, 72, 91, 68, 78, 51], lambda x: x+1, 2, 2, 0))

#Monkey 2:
#  Starting items: 78, 84, 96
#  Operation: new = old + 8
#  Test: divisible by 19
#    If true: throw to monkey 6
#    If false: throw to monkey 5

monkeys.append(Monkey([78, 84, 96], lambda x: x+8, 19, 6, 5))

#Monkey 3:
#  Starting items: 97, 86
#  Operation: new = old * old
#  Test: divisible by 3
#    If true: throw to monkey 1
#    If false: throw to monkey 0

monkeys.append(Monkey([97, 86], lambda x: x*x, 3, 1, 0))

#Monkey 4:
#  Starting items: 50
#  Operation: new = old + 6
#  Test: divisible by 13
#    If true: throw to monkey 3
#    If false: throw to monkey 1

monkeys.append(Monkey([50], lambda x: x+6, 13, 3, 1))

#Monkey 5:
#  Starting items: 73, 65, 69, 65, 51
#  Operation: new = old * 17
#  Test: divisible by 11
#    If true: throw to monkey 4
#    If false: throw to monkey 7

monkeys.append(Monkey([73, 65, 69, 65, 51], lambda x: x*17, 11, 4, 7))

#Monkey 6:
#  Starting items: 69, 82, 97, 93, 82, 84, 58, 63
#  Operation: new = old + 5
#  Test: divisible by 5
#    If true: throw to monkey 5
#    If false: throw to monkey 7

monkeys.append(Monkey([69, 82, 97, 93, 82, 84, 58, 63], lambda x: x+5, 5, 5, 7))

#Monkey 7:
#  Starting items: 81, 78, 82, 76, 79, 80
#  Operation: new = old + 3
#  Test: divisible by 17
#    If true: throw to monkey 3
#    If false: throw to monkey 4

monkeys.append(Monkey([81, 78, 82, 76, 79, 80], lambda x: x+3, 17, 3, 4))

def print_items(monkeys):
    for i in range(len(monkeys)):
        m = monkeys[i]
        print(f"Monkey {i}: {m.items}")

inspects = [0 for i in range(len(monkeys))]
to_print = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

#part 1
#for round in range(1, 21):
#    for i in range(len(monkeys)):
#        m = monkeys[i]
#        inspects[i] += len(m.items)
#        while len(m.items) > 0:
#            item = m.items.pop(0)
#            score = m.op(item)
#            score = score//3
#            result = score%m.mod==0
#            if result:
#                dest = m.true_dest
#            else:
#                dest = m.false_dest
#            to_send = score
#            monkeys[dest].items.append(to_send)


M = 1
for m in monkeys:
    M *= m.mod 
for round in range(1, 10001):
    for i in range(len(monkeys)):
        m = monkeys[i]
        inspects[i] += len(m.items)
        while len(m.items) > 0:
            item = m.items.pop(0)
            score = m.op(item)
            result = score%m.mod==0
            if result:
                dest = m.true_dest
            else:
                dest = m.false_dest
            to_send = score % M
            monkeys[dest].items.append(to_send)
    if round in to_print:
        print(f"---After round {round}---")
        print(inspects)

inspects.sort()
print(inspects[-2] * inspects[-1])
