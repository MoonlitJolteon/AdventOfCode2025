with open("input.txt") as file:
    line = file.readline()
    invalidIDs = []
    for rng in line.split(","):
        start = rng.split("-")[0]
        end = rng.split("-")[1]
        for current in range(int(start), int(end) + 1):
            current = str(current)
            if current[0] == "0":
                continue
            is_invalid = False
            for pattern_len in range(1, len(current) // 2 + 1):
                if len(current) % pattern_len == 0:
                    pattern = current[:pattern_len]
                    repetitions = len(current) // pattern_len
                    if current == pattern * repetitions and repetitions >= 2:
                        is_invalid = True
                        break
            if is_invalid:
                invalidIDs.append(int(current))
    print(sum(invalidIDs))
