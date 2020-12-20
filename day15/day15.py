from typing import List

def day15_1(startingSequence: List[int]) -> int:
    lastSeen = {}  # contains the turn number of all numbers
    spokenNums = []  # contains the numbers said starting at turn 1

    for i in range(1, 2021):
        if i < len(startingSequence):
            lastSeen[startingSequence[i - 1]] = [i]
            spokenNums.append(startingSequence[i - 1])

        elif i == len(startingSequence):
            if startingSequence[i - 1] not in lastSeen:
                spokenNums.append(startingSequence[i - 1])
                lastSeen[startingSequence[i - 1]] = [i]
                spokenNums.append(0)
            else:
                lastSeen[startingSequence[i]] = [i]
                spokenNums.append(startingSequence[i])
        else:

            if spokenNums[-1] not in lastSeen:
                spokenNums.append(0)

            else:
                lastSeen[spokenNums[-1]].append(i)
                spokenNums.append(lastSeen[spokenNums[-1]][-1] - lastSeen[spokenNums[-1]][-2])
    print(spokenNums)

print(day15_1([0,3,6]))
