tobogganTextMap = "day3.txt"

def day3_1(tobogganTextMap):
    tobogganMatrix = []
    with open(tobogganTextMap) as file:
        for line in file:
            tobogganMatrix.append(line.strip())

    file.close()

    treeCounter = 0
    position = 0
    for i in range(len(tobogganMatrix)):
        if (position >= len(tobogganMatrix[i])):
            position = position % len(tobogganMatrix[i])
        if tobogganMatrix[i][position] == "#":
            treeCounter += 1
        position += 3
    return treeCounter

print(day3_1(tobogganTextMap))