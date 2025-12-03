with open("input.txt") as rawInput:
    banks = rawInput.readlines()
    batteriesActivated = []
    for bank in banks:
        bank = bank.strip("\n")
        largestStartIndex = -1
        largestNumber = 0
        for i in range(len(bank) - 1):
            if int(bank[i]) > largestNumber:
                largestNumber = int(bank[i])
                largestStartIndex = i
        nextLargestIndex = largestStartIndex + 1
        nextLargestNumber = 0
        for i in range(nextLargestIndex, len(bank)):
            if int(bank[i]) > nextLargestNumber:
                nextLargestNumber = int(bank[i])
                nextLargestIndex = i
        batteriesActivated.append(int(str(largestNumber) + str(nextLargestNumber)))
        # print(largestNumber, nextLargestNumber)
    print(sum(batteriesActivated))
