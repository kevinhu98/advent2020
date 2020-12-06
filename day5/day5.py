inputFile = "day5.txt"

def getRow(line):
    row = -1
    rowMin = 0
    rowMax = 127
    for char in line[:7]:
        if char == "F":
            rowMax = rowMax - round(((rowMax - rowMin) / 2))
        else:  # char must be B
            rowMin = rowMin + round(((rowMax - rowMin) / 2))
    if line[6] == "F":
        row = rowMin
    else:
        row = rowMax
    return row

def getCol(line):
    col = -1
    colMin = 0
    colMax = 7
    for char in line[7:10]:
        if char == "L":
            colMax = colMax - round(((colMax - colMin) / 2))
        else:  # char must be R
            colMin = colMin + round(((colMax - colMin) / 2))
    if line[9] == "L":
        col = colMin
    else:
        col = colMax
    return col

def day5_1(inputFile):
    highestSeatID = -1
    with open(inputFile) as file:
        for line in file:
            row = getRow(line.strip())
            col = getCol(line.strip())

            if ((row * 8) + col) > highestSeatID:
                highestSeatID = (row * 8) + col

    return highestSeatID

def day5_2(inputFile):
    seatIDList = []

    with open(inputFile) as file:
        for line in file:
            row = getRow(line.strip())
            col = getCol(line.strip())

            seatIDList.append((row * 8) + col)
    file.close()
    seatIDList = sorted(seatIDList)

    total = 0
    for i in range(seatIDList[0], seatIDList[-1] + 1):
        total += i
    for digit in seatIDList:
        total -= digit
    return(total)

print(day5_2(inputFile))