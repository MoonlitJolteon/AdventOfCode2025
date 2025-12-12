# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    rows = [list(r.strip("\n")) for r in rawInput.readlines()]
beamsTracked = [rows[0].index("S")]
numSplits = 0

for i, row in enumerate(rows):
    newBeamsToTrack = []
    for beam in beamsTracked:
        if row[beam] == "^":
            numSplits += 1
            leftIndex = beam - 1
            if leftIndex >= 0:
                row[leftIndex] = "|"
                newBeamsToTrack.append(leftIndex)
            rightIndex = beam + 1
            if rightIndex < len(row):
                row[beam + 1] = "|"
                newBeamsToTrack.append(rightIndex)
        else:
            row[beam] = "|"
            newBeamsToTrack.append(beam)
    beamsTracked = list(set(newBeamsToTrack.copy()))

print("Number of splits:", numSplits)
