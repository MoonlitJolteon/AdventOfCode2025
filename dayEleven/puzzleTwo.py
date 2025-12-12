devices = []
# with open("exampleinput2.txt") as rawInput:
with open("input.txt") as rawInput:
    for line in rawInput.readlines():
        lineparts = line.strip("\n").split(" ")
        devices.append({"deviceName": lineparts[0][:-1], "outputsTo": lineparts[1:]})
    devices.append({"deviceName": "out", "outputsTo": []})

deviceMap = {device["deviceName"]: device["outputsTo"] for device in devices}

memo = {}
requiredNodes = frozenset(["fft", "dac"])


def dfsCountPathsFiltered(current, target, visited, requiredSeen):
    global memo, requiredNodes
    if current in visited:
        return 0

    state = (current, frozenset(requiredSeen))

    if state in memo:
        return memo[state]

    if current == target:
        result = 1 if requiredSeen == requiredNodes else 0
        memo[state] = result
        return result

    if current not in deviceMap:
        memo[state] = 0
        return 0

    visited.add(current)

    newRequired = requiredSeen | ({current} if current in requiredNodes else set())

    totalPaths = 0
    for nextDevice in deviceMap[current]:
        totalPaths += dfsCountPathsFiltered(nextDevice, target, visited, newRequired)

    visited.remove(current)

    memo[state] = totalPaths
    return totalPaths


print("Starting path counting...")
num_paths = dfsCountPathsFiltered("svr", "out", set(), frozenset())
print(f"Number of paths: {num_paths}")
