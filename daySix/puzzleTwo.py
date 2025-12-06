import math
import numpy as np


def rotateTextFile(inputFilename, outputFilename):
    rawLines = []
    readyToProcessLines = []
    with open(inputFilename) as rawInput:
        rawLines = [line.rstrip("\n") for line in rawInput.readlines()]
        max_len = max(len(line) for line in rawLines) if rawLines else 0
        readyToProcessLines = [list(line.ljust(max_len)) for line in rawLines]

    rotated = np.rot90(readyToProcessLines)

    with open(outputFilename, "w") as f_out:
        for row in rotated:
            f_out.write("".join(row) + "\n")


rotateTextFile("input.txt", "intermediate.txt")

operations = []
results = []
with open("intermediate.txt") as rawInput:
    operation = []
    lines = rawInput.readlines()
    for i, line in enumerate(lines):
        if len(line.strip(" ").strip("\n")) > 0:
            operator = None
            try:
                currNum = int(line)
            except ValueError:
                currNum = int(line[0:-2])
                operator = line[-2]

            operation.append(currNum)
            if operator is not None:
                operation.append(operator)
                if operation[-1] == "+":
                    results.append(sum(operation[0:-1]))
                else:
                    results.append(math.prod(operation[0:-1]))
                operator = None

                operation.append(results[-1])
                operations.append(operation.copy())
                operation = []

# print(operations)
print(sum(results))
