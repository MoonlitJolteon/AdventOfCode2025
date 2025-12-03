with open("input.txt") as rawInput:
    banks = rawInput.readlines()
    batteriesActivated = []
    for bank in banks:
        bank = bank.strip("\n")
        k = 12
        to_remove = len(bank) - k
        stack = []
        for digit in bank:
            while stack and to_remove > 0 and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        result = "".join(stack[:k])
        batteriesActivated.append(int(result))
    print(sum(batteriesActivated))
