with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

baselines = {"X": 1, "Y": 2, "Z": 3}
results = {("A", "X"): 3, ("A", "Y"): 6, ("A", "Z"): 0, ("B", "X"): 0, ("B", "Y"): 3, ("B", "Z"): 6, ("C", "X"): 6, ("C", "Y"): 0, ("C", "Z"): 3}
tot = 0

for line in lines:
    (opp, me) = line.split(" ")
    result = results[(opp, me)]
    baseline = baselines[me]
    tot += result + baseline

print(tot)

tot = 0
baselines = {"A": 1, "B": 2, "C": 3}
results = {"X": 0, "Y": 3, "Z": 6}
plays = {("A", "X"): "C", ("A", "Y"): "A", ("A", "Z"): "B", ("B", "X"): "A", ("B", "Y"): "B", ("B", "Z"): "C", ("C", "X"): "B", ("C", "Y"): "C", ("C", "Z"): "A"}
for line in lines:
    (opp, result) = line.split(" ")
    play = plays[(opp, result)] 
    tot += results[result] + baselines[play]

print(tot)
            
