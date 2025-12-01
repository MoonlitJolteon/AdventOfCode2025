dial = 50
numberOfZeros = 0
with open("combo.txt") as combo:
    directions = combo.readlines()
    for instruction in directions:
        instruction = instruction.strip("\n")
        direction = instruction[0]
        amount = instruction[1:]

        # Part 1 code below
        # if direction == "L":
        #     dial -= int(amount)
        # else:
        #     dial += int(amount)
        # dial = dial % 100
        # if dial == 0:
        #     numberOfZeros += 1
        # print(dial)
        # Part 2 code above

        # Part 2 code below
        for _ in range(int(amount)):
            if direction == "L":
                dial -= 1
            else:
                dial += 1
            dial = dial % 100
            if dial == 0:
                print("clicked at 0")
                numberOfZeros += 1
        # Part 2 code above
    print(numberOfZeros)
