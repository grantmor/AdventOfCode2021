def main():
    with open('input', 'r') as file:
        print(
            count_increases(
                compute_window_averages(
                    list(
                        map(int, file.read().split())))))


def compute_window_averages(data):
    idx = 0

    averages = []

    while idx + 2 < len(data):
        windowAvg = sum(data[idx:idx+3]) / 3
        averages.append(windowAvg)
        idx += 1

    return averages


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
