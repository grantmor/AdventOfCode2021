class Command:
    def __init__(self, commandList):
        self.action = commandList[0]
        self.magnitude = int(commandList[1])


def process_file(filePath):
    with open(filePath, 'r') as file:
        commands = file.read().strip().split('\n')
        commands = [command.split() for command in commands]
        commands = [Command(command) for command in commands]

    return commands

def predict_course(comBuf):
    hPos = 0
    depth = 0

    for com in comBuf:
        if com.action == 'forward':
            hPos += com.magnitude
        elif com.action == 'down':
            depth += com.magnitude
        elif com.action == 'up':
            depth -= com.magnitude
    
    return {'hPos': hPos, 'depth': depth}



def main():
    comBuf = process_file('input')
    location = predict_course(comBuf)
    print(location['hPos'] * location['depth'])

main()