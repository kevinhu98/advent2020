
def day12_1(inputFile):
    with open(inputFile) as f:
        commands = [line.strip() for line in f]
    cardinalDirections = ["N", "E", "S", "W"]
    distances = {"N": 0, "S": 0, "E": 0, "W": 0}
    currDirection = "E"  # ship direction always starts east

    for movement in commands:
        movementDirection = movement[0]
        movementDistance = int(movement[1:])

        if movementDirection in cardinalDirections:
            distances[movementDirection] += movementDistance

        elif movementDirection == "F":
            distances[currDirection] += movementDistance

        elif movementDirection in ["L", "R"]:
            totalTurns = movementDistance / 90

            if movementDirection == "L":
                currDirectionIndex = cardinalDirections.index(currDirection)
                currDirection = cardinalDirections[int(currDirectionIndex - totalTurns)]

            else:
                currDirectionIndex = cardinalDirections.index(currDirection)
                currDirection = cardinalDirections[int((currDirectionIndex + totalTurns) % 4)]

    return abs(distances["N"] - distances["S"]) + abs(distances["E"] - distances["W"])


if __name__ == "__main__":
    print(day12_1("day12.txt"))