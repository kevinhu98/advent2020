inputFile = "day4.txt"

def day4_1(inputFile):
    with open(inputFile) as file:
        valid = 0
        attributes = {}
        for line in file:
            if line != "\n":  # read in each line until blank line
                for pair in line.split():
                    pair = pair.split(":")
                    attributes[pair[0]] = pair[1]  # turn each value into key value pair
            else:
                if len(attributes) == 8:  # if there are 8 pairs, is valid
                    valid += 1
                elif len(attributes) == 7:  # if 7 pairs without cid, is valid
                    if "cid" not in attributes:
                        valid += 1
                attributes = {}  # reset attribute dict after every blank line
    file.close()
    return valid

#print(day4_1(inputFile))

def checkValidBirthYear(attributes):
    return 1920 <= int(attributes["byr"]) <= 2002  # at least 1920 and at most 2002

def checkValidIssueYear(attributes):
    return 2010 <= int(attributes["iyr"]) <= 2020  # at least 2010 and at most 2020

def checkValidExpirationYear(attributes):
    return 2020 <= int(attributes["eyr"]) <= 2030  # at least 2020 and at most 2030

def checkValidHeight(attributes):
    if attributes["hgt"][-2:] == "in":  # a number followed by either cm or in
        return 59 <= int(attributes["hgt"][:-2]) <= 76  # If cm, the number must be at least 150 and at most 193
    elif attributes["hgt"][-2:] == "cm":  # a number followed by either cm or in
        return 150 <= int(attributes["hgt"][:-2]) <= 193  # If in, the number must be at least 59 and at most 76
    return False

def checkValidHairColor(attributes):
    if len(attributes["hcl"]) != 7:  # must be len 7
        return False

    valid = []  # list of all valid characters 0-9, a-f

    for i in range(10):  # append valid digits 0-9
        valid.append(str(i))

    for char in "abcdef":  # append valid letters a-f
        valid.append(char)

    if attributes["hcl"][0] != "#":  # check first character is pound
        return False

    for i in range(1, len(attributes["hcl"])):  # check if characters are valid
        if attributes["hcl"][i] not in valid:
            return False
    return True

def checkValidEyeColor(attributes):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if attributes["ecl"] not in valid:  # exactly one of: amb blu brn gry grn hzl oth
        return False

    return True

def checkValidPassportID(attributes):
    return len(attributes["pid"]) == 9

def checkValid(attributes:dict) -> bool:
    attributeFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    if len(attributes) < 7:
        return False
    elif (len(attributes) == 7 and "cid" not in attributes) or len(attributes) == 8:
        if not checkValidBirthYear(attributes):
            return False
        elif not checkValidIssueYear(attributes):
            return False
        elif not checkValidExpirationYear(attributes):
            return False
        elif not checkValidHeight(attributes):
            return False
        elif not checkValidHairColor(attributes):
            return False
        elif not checkValidEyeColor(attributes):
            return False
        elif not checkValidPassportID(attributes):
            return False
        return True

def day4_2(inputFile):
    with open(inputFile) as file:
        valid = 0
        attributes = {}
        for line in file:
            if line != "\n":
                for pair in line.split():
                    pair = pair.split(":")
                    attributes[pair[0]] = pair[1]
            else:
                if checkValid(attributes):
                    valid += 1
                attributes = {}
    file.close()
    return valid

print(day4_2(inputFile))