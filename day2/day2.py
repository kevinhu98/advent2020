passwordList = "day2.txt"

def day2_1(passwordList):
    validCount = 0
    with open(passwordList) as file:
        for line in file:
            letterCount = 0
            line = line.strip().split()  # remove trailing \n and separate into list
            minAppearance = int(line[0].split("-")[0])
            maxAppearance = int(line[0].split("-")[1])
            character = line[1][0]  # isolate letter

            for letter in line[2]:  # check how many times character appears in string
                if letter == character:
                    letterCount += 1

            if minAppearance <= letterCount <= maxAppearance:  # check if count is within accepted range
                validCount += 1

    return validCount

print(day2_1(passwordList))

def day2_2(passwordList):
    validCount = 0
    with open(passwordList) as file:
        for line in file:
            seenCount = 0
            line = line.strip().split()  # remove trailing \n and separate into list
            firstIndexCheck = int(line[0].split("-")[0])-1  # subtract 1 since index starts at 1
            secondIndexCheck = int(line[0].split("-")[1])-1  # subtract 1 since index starts at 1
            character = line[1][0]  # isolate letter

            if line[2][firstIndexCheck] == character:  # check if the character appears at specified location
                seenCount += 1
            if line[2][secondIndexCheck] == character:  # check if the character appears at specified location
                seenCount += 1
            if seenCount == 1:  # check if character appears only once in the two spots
                validCount += 1

    return validCount

print(day2_2(passwordList))