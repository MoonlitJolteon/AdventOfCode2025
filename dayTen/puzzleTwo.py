import re
from pulp import *

# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    machines = []
    for line in rawInput.readlines():
        lightsNeeded = re.findall(r"\[(.*?)\]", line)[0]
        buttons = [button.split(",") for button in re.findall(r"\((.*?)\)", line)]
        joltageRequired = re.findall(r"\{(.*?)\}", line)[0]
        machines.append(
            {
                "lightTargetStatus": lightsNeeded,
                "buttons": buttons,
                "joltageRequired": joltageRequired,
            }
        )


def incrementLightCount(state, buttonIndices):
    stateList = list(state)
    for i in buttonIndices:
        stateList[int(i)] += 1
    return tuple(stateList)


currentMachineCount = 0


def solve(machine):
    target = [int(x) for x in machine["joltageRequired"].split(",")]
    buttons = machine["buttons"]

    problem = LpProblem("MinButtonPresses", LpMinimize)

    buttonVariables = [
        LpVariable(f"button{i}", lowBound=0, cat="Integer") for i in range(len(buttons))
    ]

    problem += lpSum(buttonVariables)

    for lightIndex in range(len(target)):
        lightSum = lpSum(
            [
                buttonVariables[bIdx]
                for bIdx, button in enumerate(buttons)
                if str(lightIndex) in button
            ]
        )
        problem += lightSum == target[lightIndex]

    problem.solve(PULP_CBC_CMD(msg=0))

    if problem.status == 1:
        return int(value(problem.objective))
    return -1


solutions = [solve(machine) for machine in machines]
print(sum(solutions))
