def day8_1(inputFile):
    commands = []  # list of instructions
    position = 0  # instruction position
    acc = 0  # accumulator value
    seen = []  # instruction position that have been visited

    with open(inputFile) as file:
        for line in file:
            commands.append(line.strip())

    while position not in seen:  # if seen previous instruction, means loop
        if position not in seen:
            seen.append(position)

        operation = commands[position][0:3]
        sign = commands[position][4]
        value = commands[position][5:]

        if operation == "acc":
            if sign == "+":
                acc += int(value)
            else:
                acc -= int(value)
            position += 1
        elif operation == "jmp":
            if sign == "+":
                position += int(value)
            else:
                position -= int(value)
        elif operation == "nop":
            position += 1
    return acc


def day8_2(inputFile):
    commands = []

    with open(inputFile) as file:
        for line in file:
            commands.append(line.strip())

    for i in range(len(commands)):  # same as pt 1, but make one instruction change at a time
        commandsCopy = list(commands)
        if commands[i][0:3] == "nop":
            commandsCopy[i] = commandsCopy[i].replace("nop", "jmp")
        elif commands[i][0:3] == "jmp":
            commandsCopy[i] = commandsCopy[i].replace("jmp", "nop")

        position = 0
        acc = 0
        seen = []

        while position not in seen:
            try:
                if position not in seen:
                    seen.append(position)

                operation = commandsCopy[position][0:3]
                sign = commandsCopy[position][4]
                value = commandsCopy[position][5:]

                if operation == "acc":
                    if sign == "+":
                        acc += int(value)
                    else:
                        acc -= int(value)
                    position += 1
                elif operation == "jmp":
                    if sign == "+":
                        position += int(value)
                    else:
                        position -= int(value)
                elif operation == "nop":
                    position += 1
            except IndexError:  # if index out of bounds, means finished instructions
                return acc

if __name__ == "__main__":
    inputFile = "day8.txt"

    #print(day8_1(inputFile))
    print(day8_2(inputFile))