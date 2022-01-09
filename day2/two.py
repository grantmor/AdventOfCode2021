class Command:
    def __init__(self, commandList):
        self.action = commandList[0]
        self.magnitude = int(commandList[1])


def process_file(filePath):
    with open(filePath, 'r') as file:
        # Simply reassigning commands would save 2n memory, but this is clearer
        lines = file.read().strip().split('\n')
        commandList = [line.split() for line in lines]
        commandObjs = [Command(command) for command in commands]

    return commandsObjs


def predict_course(comBuf):
    aim = 0
    hPos = 0
    depth = 0

    for com in comBuf:
        if com.action == 'forward':
            hPos += com.magnitude
            depth += aim * com.magnitude
        elif com.action == 'down':
            aim += com.magnitude
        elif com.action == 'up':
            aim -= com.magnitude
    
    return {'hPos': hPos, 'depth': depth}


def main():
    commandBuffer = process_file('input')
    location = predict_course(commandBuffer)
    print(location['hPos'] * location['depth'])


main()