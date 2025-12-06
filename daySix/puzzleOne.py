import math

lines = []
with open("input.txt") as rawInput:
    for line in rawInput.readlines():
        lines.append(list(filter(None, line.strip("\n").split(" "))))

results = []
for i in range(len(lines[0])):
    operation = lines[-1][i]
    toCalculate = []
    for j in range(len(lines) - 1):
        toCalculate.append(int(lines[j][i]))
    if operation == "+":
        results.append(sum(toCalculate))
    else:
        results.append(math.prod(toCalculate))
print(sum(results))
