def update(layout: [[]]) -> [[]]:
    defaultLayout = layout
    for i in range(len(layout)):  # row
        for j in range(len(layout[0])):  # col
            upCheck, leftCheck, rightCheck, downCheck = False, False, False, False  # if check true = occupied
            if j > 0:
                if defaultLayout[i][j-1] == "#":
                    leftCheck = True

            if j < len(defaultLayout[0]) - 1:
                if defaultLayout[i][j+1] == "#":
                    rightCheck = True

            if i > 0:
                if defaultLayout[i-1][j] == "#":
                    upCheck = True

            if i < len(defaultLayout) - 1:
                if defaultLayout[i+1][j] == "#":
                    downCheck = True

            if upCheck == leftCheck == rightCheck == downCheck == False:  # if seat empty and no occupied seats adjacent
                if layout[i][j] == 'L':
                    layout[i][j] = "#"
            elif upCheck == leftCheck == rightCheck == downCheck == True:
                if layout[i][j] == '':
                    layout[i][j] = "L"
    for row in layout:
        print(row)

def day11_1(inputFile):
    layout = []
    with open(inputFile) as file:
        for line in file:
            layout.append([char for char in line.strip()])
    file.close()

    for row in layout:
        print(row)
    print('kek')
    print(update(layout))

if __name__ == "__main__":
    inputFile = "day11.txt"
    print(day11_1(inputFile))