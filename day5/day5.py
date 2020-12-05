inputFile = "day5.txt"
#break into getrow, get column get seatID
def day5_1(inputFile):
    highestSeatID = -1

    with open(inputFile) as file:

        for line in file:
            row = -1
            column = -1

            rowMin = 0
            rowMax = 127

            colMin = 0
            colMax = 7


            line = line.strip()
            for char in line[:7]:
                if char == "F":
                    rowMax = rowMax - round(((rowMax - rowMin) / 2))
                else:  # char must be B
                    rowMin = rowMin + round(((rowMax - rowMin) / 2))

            if line[6] == "F":
                row = rowMin
            else:
                row = rowMax

            for char in line[7:10]:
                if char == "L":
                    colMax = colMax - round(((colMax - colMin) / 2))
                else:  # char must be R
                    colMin = colMin + round(((colMax - colMin) / 2))

            if line[9] == "L":
                col = colMin
            else:
                col = colMax

            if ((row * 8) + col) > highestSeatID:
                highestSeatID = (row * 8) + col

    return highestSeatID
print(day5_1(inputFile))