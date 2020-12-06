inputFile = "day6.txt"

def day6_1(inputFile):
    total = 0
    with open(inputFile) as file:
        yesAnswers = []
        for line in file:
            if line != "\n":
                for char in line.strip():
                    if char not in yesAnswers:  # if char not already seen
                        yesAnswers.append(char)
            else:
                total += len(yesAnswers)
                yesAnswers = []

        total += len(yesAnswers)  # add remaining yes if last line not "\n"
    file.close()
    return total

print(day6_1(inputFile))

def day6_2(inputFile):
    total = 0
    with open(inputFile) as file:
        groupCount = 0  # how many people are in a group
        yesCount = {}  # dict where key = answer, val = answer count
        for line in file:
            if line != "\n":
                groupCount += 1
                for char in line.strip():
                    if char in yesCount:
                        yesCount[char] += 1  # if answer in dict, increment answer count
                    else:
                        yesCount[char] = 1  # otherwise, set answer count to 1
            else:
                for key,val in yesCount.items():
                    if val == groupCount:  # increment if answer appears equal to num in group
                        total += 1
                groupCount = 0
                yesCount = {}

        for key, val in yesCount.items():  # check leftover since file does not end in "\n"
            if val == groupCount:
                total += 1
    file.close()
    return total

print(day6_2(inputFile))