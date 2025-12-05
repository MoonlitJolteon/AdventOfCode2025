def combineRanges(ranges):
    ranges.sort(key=lambda x: x["start"])

    merged = []
    for current in ranges:
        if not merged or merged[-1]["end"] < current["start"] - 1:
            merged.append(current.copy())
        else:
            merged[-1]["end"] = max(merged[-1]["end"], current["end"])

    return merged


with open("input.txt") as rawInput:
    isReadingRanges = True
    freshIDRanges = []
    for line in [l.strip("\n") for l in rawInput.readlines()]:
        if len(line) == 0:
            break

        startEnd = line.split("-")
        rang = {"start": int(startEnd[0]), "end": int(startEnd[1])}
        freshIDRanges.append(rang)

    freshIDRanges = combineRanges(freshIDRanges)

    numFreshIngredients = 0
    for range in freshIDRanges:
        numFreshIngredients += range["end"] - range["start"] + 1

    print(numFreshIngredients)
