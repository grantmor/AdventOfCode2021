import sys

DAYS_UNTIL_ADULTHOOD = 8
DAYS_TO_REPRODUCE = 6


def read_input(path):
    with open(path, 'r') as file:
        return list(map(int, file.read().strip().split(',')))


def advance_day(fishTable):
    reproducingFish = fishTable[0]

    # Age all fish one day
    for fish in fishTable:
        if fish != 0:
            fishTable[fish - 1] = fishTable[fish]
    
    # New fish born
    fishTable[DAYS_UNTIL_ADULTHOOD] = reproducingFish
    # Old fish reproduce in 6 days
    fishTable[DAYS_TO_REPRODUCE] += reproducingFish

    return fishTable


def run_simulation(numDays):
    fishList = read_input(sys.argv[1])

    # Hash Tables are fast
    fishTable = {}

    # Initialize fishtable
    for val in range(0, 8):
        fishTable[val] = 0

    # Populate fishtable
    for fish in fishList:
        if fish not in fishTable:
            fishTable[fish] = 1
        else:
            fishTable[fish] += 1

    # Simulate population growth
    for day in range(0, numDays):
        fishTable = advance_day(fishTable)

    # Accumulate # of total fish
    totalFish = 0
    for fish in fishTable:
        totalFish += fishTable[fish]

    return totalFish


print(run_simulation(256))