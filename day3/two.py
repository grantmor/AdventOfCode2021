import sys
from math import ceil

def process_input():
    with open(sys.argv[1], 'r') as file:
        input = file.read().strip().split()
    return input

def most_common_value(words, chrIndex):
    ones = 0
    zeros = 0

    for word in words:
        if word[chrIndex] == '1':
            ones += 1
        else:
            zeros += 1

    if ones == zeros:
        return 'equal'
    elif ones > zeros:
        return '1'
    elif ones < zeros:
        return '0'


def O2_rating_calc(words, chrIndex):
    if len(words) <= 1:
        return words[0]

    curMostCommonVal = most_common_value(words, chrIndex)
    remainingWords = []

    for word in words:
        curChr = word[chrIndex]
        if curChr == curMostCommonVal or (curMostCommonVal == 'equal' and curChr == '1'):
            remainingWords.append(word)

    return O2_rating_calc(remainingWords, chrIndex + 1)


def cO2_rating_calc(words, chrIndex):
    if len(words) == 1:
        return words[0]

    curMostCommonVal = most_common_value(words, chrIndex)
    if curMostCommonVal == '0':
        leastCommonVal = '1'
    elif curMostCommonVal == '1':
        leastCommonVal = '0'
    elif curMostCommonVal == 'equal':
        leastCommonVal = 'equal'

    remainingWords = []

    for word in words:
        curChr = word[chrIndex]
        if (curChr == leastCommonVal or (leastCommonVal == 'equal' and curChr == '0')):
            remainingWords.append(word)

    return cO2_rating_calc(remainingWords, chrIndex + 1)


def decimal_from_binary_string(string):
    reversed = ''

    idx = len(string) - 1
    while idx >= 0:
        reversed += string[idx]
        idx -= 1

    #print(reversed)
    
    place = 1
    value = 0
    for char in reversed:
        value += (place * int(char))
        place *= 2
    
    return value


input = process_input()

oxygenRating = decimal_from_binary_string(O2_rating_calc(input, 0))
cO2Rating = decimal_from_binary_string(cO2_rating_calc(input, 0))

print(oxygenRating * cO2Rating)
