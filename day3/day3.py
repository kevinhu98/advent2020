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
        if position >= len(tobogganMatrix[i]):
            position = position % len(tobogganMatrix[i])
        if tobogganMatrix[i][position] == "#":
            treeCounter += 1
        position += 3
    return treeCounter

print(day3_1(tobogganTextMap))

def day3_2(tobogganTextMap):
    tobogganMatrix = []
    with open(tobogganTextMap) as file:
        for line in file:
            tobogganMatrix.append(line.strip())
    file.close()

    movement = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # first sub-index is right and second is down i.e[5,1] is right 5 down 1

    treeProduct = 1
    for i in range(len(movement)):
        treeCounter = 0
        position = 0
        for j in range(0, len(tobogganMatrix), movement[i][1]):

            if position >= len(tobogganMatrix[j]):
                position = position % len(tobogganMatrix[j])
            if tobogganMatrix[j][position] == "#":
                treeCounter += 1
            position += movement[i][0]
        treeProduct *= treeCounter
    return treeProduct

print(day3_2(tobogganTextMap))