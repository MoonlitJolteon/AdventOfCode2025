import re
from collections import deque

# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    machines = []
    for line in rawInput.readlines():
        lightsNeeded = re.findall(r"\[(.*?)\]", line)[0]
        buttons = [button.split(",") for button in re.findall(r"\((.*?)\)", line)]
        joltageRequired = re.findall(r"\{(.*?)\}", line)[0].split(",")
        machines.append(
            {
                "lightTargetStatus": lightsNeeded,
                "buttons": buttons,
                "joltageRequired": joltageRequired,
            }
        )


def toggleLights(stateStr, buttonIndices):
    stateList = list(stateStr)
    for i in buttonIndices:
        i = int(i)
        if stateList[i] == ".":
            stateList[i] = "#"
        else:
            stateList[i] = "."
    return "".join(stateList)


def breadthFirstSolve(machine):
    target = machine["lightTargetStatus"]
    initialState = "." * len(target)
    buttons = machine["buttons"]

    if initialState == target:
        return 0

    queue = deque([(initialState, 0)])
    visited = {initialState}

    while queue:
        currentState, presses = queue.popleft()

        for button in buttons:
            newState = toggleLights(currentState, button)

            if newState == target:
                return presses + 1

            if newState not in visited:
                visited.add(newState)
                queue.append((newState, presses + 1))
    return -1


solutions = [breadthFirstSolve(machine) for machine in machines]
print(sum(solutions))
