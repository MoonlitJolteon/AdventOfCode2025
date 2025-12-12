# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    rows = [list(r.strip("\n")) for r in rawInput.readlines()]

counts = {rows[0].index("S"): 1}
numSplits = 0

for i, row in enumerate(rows):
    newCounts = {}
    for beam, count in counts.items():
        if row[beam] == "^":
            numSplits += count

            leftIndex = beam - 1
            if leftIndex >= 0:
                row[leftIndex] = "|"
                newCounts[leftIndex] = newCounts.get(leftIndex, 0) + count

            rightIndex = beam + 1
            if rightIndex < len(row):
                row[rightIndex] = "|"
                newCounts[rightIndex] = newCounts.get(rightIndex, 0) + count
        else:
            row[beam] = "|"
            newCounts[beam] = newCounts.get(beam, 0) + count

    counts = newCounts

print("Number of timelines:", sum(counts.values()))
