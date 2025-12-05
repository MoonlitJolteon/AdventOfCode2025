with open("input.txt") as rawInput:
    isReadingRanges = True
    freshIDRanges = []
    freshIDs = []
    for line in [l.strip("\n") for l in rawInput.readlines()]:
        if len(line) == 0:
            isReadingRanges = False
            continue

        if isReadingRanges:
            startEnd = line.split("-")
            freshIDRanges.append({"start": int(startEnd[0]), "end": int(startEnd[1])})
        else:
            for currentCheckingRange in freshIDRanges:
                if (
                    int(line) >= currentCheckingRange["start"]
                    and int(line) <= currentCheckingRange["end"]
                ) and int(line) not in freshIDs:
                    freshIDs.append(int(line))

    print(len(freshIDs))
