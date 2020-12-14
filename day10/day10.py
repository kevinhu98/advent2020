from collections import Counter

def day10_1(inputFile):
    joltages = [0]  # default joltage comparison is 0
    differences = {1: 0, 2: 0, 3: 0}  # highest difference always of 3
    with open(inputFile) as file:
        for line in file:
            joltages.append(int(line.strip()))
    file.close()

    joltages = sorted(joltages)
    joltages.append(max(joltages) + 3)  # max joltage is +3 the found max

    for i in range(len(joltages)-1):
        difference = joltages[i+1] - joltages[i]
        differences[difference] += 1

    return differences


def day10_2(inputFile):
    joltages = [0]
    c = Counter({0:1})  # default joltage comparison is 0
    differences = {1: 0, 2: 0, 3: 0}  # highest difference always of 3
    with open(inputFile) as file:
        for line in file:
            joltages.append(int(line.strip()))
    file.close()

    joltages = sorted(joltages)
    joltages.append(max(joltages) + 3)  # max joltage is +3 the found max


    for num in joltages:  # each adapter has its value set by its previous 3 adapters
        c[num + 1] += c[num]
        c[num + 2] += c[num]
        c[num + 3] += c[num]

    print(c)
    return c[max(joltages)]
if __name__ == "__main__":
    inputFile = "day10mini.txt"
    print(day10_1(inputFile))
    print(day10_2(inputFile))
