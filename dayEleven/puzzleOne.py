devices = []
# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    for line in rawInput.readlines():
        lineparts = line.strip("\n").split(" ")
        devices.append({"deviceName": lineparts[0][:-1], "outputsTo": lineparts[1:]})
    devices.append({"deviceName": "out", "outputsTo": []})

deviceMap = {device["deviceName"]: device["outputsTo"] for device in devices}


def dfsCountPaths(current, target, visited):
    if current == target:
        return 1

    if current not in deviceMap:
        return 0

    if current in visited:
        return 0

    visited.add(current)

    totalPaths = 0
    for nextDevice in deviceMap[current]:
        totalPaths += dfsCountPaths(nextDevice, target, visited)

    visited.remove(current)

    return totalPaths


print("Starting path counting...")
num_paths = dfsCountPaths("you", "out", set())
print(f"Number of paths: {num_paths}")
