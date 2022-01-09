import sys

class Board:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = []
        self.marked = []

    def appendRow(self, row):
        #print(f'appending row: {row}')
        self.data.append(row)
        self.rows += 1

        # dynamic number of rows /cols make this slower ( O(n) )
        # will optimize this out if not needed
        rowLength = len(row)
        if rowLength > self.cols:
            self.cols = rowLength
    
    def markNumber(self, number):
        #print('markNumber called with ' + str(number))
        rowIdx = 0
        colIdx = 0

        # Does this really count as quadratic? The board doens't grow...
        #print(self.rows)
        #print(self.cols)
        while rowIdx < self.rows:
            colIdx = 0
            while colIdx < self.cols:
                if self.data[rowIdx][colIdx] == number:
                    self.marked.append((rowIdx, colIdx))
                    #print('appending' + (rowIdx, colIdx))
                colIdx += 1
            rowIdx += 1
    
    def checkWin(self):
        rowHits = {}
        colHits = {}

        # Hash Table - number of occurances of each rownum/colnum
        for markedCell in self.marked:
            if markedCell[0] in rowHits:
                rowHits[markedCell[0]] += 1
            else:
                rowHits[markedCell[0]] = 1
            if markedCell[1] in colHits:
                colHits[markedCell[1]] += 1
            else:
                colHits[markedCell[1]] = 1
        
        for row in rowHits:
            if rowHits[row] == self.rows:
                return True
        
        for col in colHits:
            if colHits[col] == self.cols:
                return True
        
        return False

    def sum(self):
        row = 0
        col = 0
        total = 0

        while row < self.rows:
            col = 0
            while col < self.cols:
                #print('NEW COL')
                #print(f'rowIdx: {rowIdx}')
                #print(f'colIdx: {colIdx}')
                if not ((row, col) in self.marked):
                    total += self.data[row][col]
                #print(f'{row}, {col} NOT IN MARKED!!!')
                col += 1
            row += 1
        return total


def read_input():
    with open(sys.argv[1], 'r') as file:
        return file.read().split("\n")


def process_input(lines):
    #print(lines)
    def filter_spaces(chr):
        if chr == ' ':
            return False
        else:
            return True

    
    drawnNumbers = lines[0].split(',')
    drawnNumbers = list(map(int, drawnNumbers))
    
    #for line in lines[1:]:
        #print(line.split())
        #line = list(filter(filter_spaces, line))
        #print(line)

    boards = []

    # iterate through remaining input and instantiate boards
    lastLineEmpty = False
    #print(lines[1:])
    for line in lines[1:]:
        if line == '':
            #print("newline")
            lastLineEmpty = True
            continue
        else:
            line = list(map(int, line.split()))
            #print(f'line:{line}')

            if lastLineEmpty == True:
                board = Board()
                board.appendRow(line)
                boards.append(board)
            else:
                boards[len(boards)-1].appendRow(line)

            lastLineEmpty = False

    return (drawnNumbers, boards)

def run_game():
    drawnNumbers, boards = process_input(read_input())

    #print(f'drawnNumbers:{drawnNumbers}')
    
    #for board in boards:
    #    for row in board.data:
    #        print(row)
            

    for num in drawnNumbers:
        for board in boards:
            board.markNumber(num)
            if board.checkWin():
                #print(f'board.sum(): {board.sum()}')
                return(board.sum() * num)


print(run_game())



