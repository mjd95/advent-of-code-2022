with open("test") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

payload = lines[0]

for i in range(4, len(payload)):
    if len(set(payload[i-4:i])) == 4:
        print(i)
        break

for i in range(14, len(payload)):
    if len(set(payload[i-14:i])) == 14:
        print(i)
        break
