# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    tiles = [tuple(map(int, line.split(","))) for line in rawInput]

print(
    max(
        (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
    )
)
