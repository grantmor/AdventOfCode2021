def main():
    with open("input", 'r') as file:
        data = file.read().split()

    data = list(map(int, data))
    print(count_increases(data))

def count_increases(data):
    numReadings = len(data)

    idx = 0
    increases = 0


    while idx < numReadings:
        if numReadings > 0:
            if data[idx - 1] < data[idx]:
                increases += 1
        idx += 1

    return increases



main()


