# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    lines = [line.strip() for line in rawInput.readlines()]

shapeSizes = {}
validCount = 0

for i, line in enumerate(lines):
    if ":" in line and "x" not in line:
        idx = int(line.split(":")[0])
        count = 0
        j = i + 1
        while j < len(lines) and lines[j] and ":" not in lines[j]:
            count += lines[j].count("#")
            j += 1
        shapeSizes[idx] = count
    elif "x" in line and ":" in line:
        dims, counts = line.split(":")
        width, height = map(int, dims.split("x"))
        counts = list(map(int, counts.split()))
        cellsNeeded = sum(
            count * shapeSizes.get(i, 0) for i, count in enumerate(counts)
        )
        if cellsNeeded <= width * height:
            validCount += 1

print(validCount)
