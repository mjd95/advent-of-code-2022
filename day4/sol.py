with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

tot = 0
tot2 = 0
for line in lines:
    first, second = line.split(",")
    first_start, first_end = [int(a) for a in first.split("-")]
    second_start, second_end = [int(a) for a in second.split("-")]

    if first_start >= second_start and first_end <= second_end:
        tot += 1
    elif second_start >= first_start and second_end <= first_end:
        tot += 1

    if first_start >= second_start and first_start <= second_end:
        tot2 += 1
    elif first_end >= second_start and first_end <= second_end:
        tot2 += 1
    elif second_start >= first_start and second_end <= first_end:
        tot2 += 1
    elif second_end >= first_start and second_end <= first_end:
        tot2 += 1

print(tot)
print(tot2)

