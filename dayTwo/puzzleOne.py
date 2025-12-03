with open("input.txt") as file:
    line = file.readline()
    invalidIDs = []
    for rng in line.split(","):
        start = rng.split("-")[0]
        end = rng.split("-")[1]
        for current in range(int(start), int(end) + 1):
            current = str(current)
            # Skip numbers with leading zeroes
            if current[0] == "0":
                continue
            # Check if the ID is a pattern repeated exactly twice
            # The pattern must be exactly half the length of the number
            if len(current) % 2 == 0:
                half = len(current) // 2
                pattern = current[:half]
                if current == pattern + pattern:
                    invalidIDs.append(int(current))
    print(sum(invalidIDs))
