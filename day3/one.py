import sys

def process_input():
    with open(sys.argv[1], 'r') as file:
        input = file.read().strip().split()
    return input

def compute_gamma(words):
    wordLength = len(words[0])
    numWords = 0

    for word in words:
        numWords += 1

    gamma_rate = ''
    zeros = 0
    index = 0

    while index < wordLength:

        for word in words:
            if word[index] == '0':
                zeros += 1
        if zeros > (numWords // 2): 
            gamma_rate += '0'
        else:
            gamma_rate += '1'
        
        zeros = 0
        index += 1

    return gamma_rate

def epsilon_from_gamma(gamma):
    epsilon = ''

    charIdx = 0
    while charIdx < len(gamma):
        if gamma[charIdx] == '0':
            epsilon += '1'
        else:
            epsilon += '0'
        charIdx += 1

    return epsilon


def decimal_from_binary_string(str):
    reversed = ''

    idx = len(str) - 1
    while idx >= 0:
        reversed += str[idx]
        idx -= 1
    print(reversed)
    
    place = 1
    value = 0
    for char in reversed:
        value += (place * int(char))
        place *= 2
    
    return value


gamma = compute_gamma(process_input())
epsilon = epsilon_from_gamma(gamma)


print (decimal_from_binary_string(gamma) *  decimal_from_binary_string(epsilon))
