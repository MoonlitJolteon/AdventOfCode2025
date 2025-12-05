with open("input.txt") as rawInput:
    grid = [list(line.strip()) for line in rawInput.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while True:
        accessible_count_this_iteration = 0
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "@":
                                adjacent_rolls += 1

                    if adjacent_rolls < 4:
                        to_remove.append((r, c))
                        accessible_count_this_iteration += 1

        for r, c in to_remove:
            grid[r][c] = "."
            accessible_count += 1

        if accessible_count_this_iteration == 0:
            break

    print(accessible_count)
