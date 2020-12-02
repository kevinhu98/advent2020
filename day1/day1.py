def day1_1():
    seen = []
    with open("day1.txt") as file:
        for line in file:
            num = int(line)
            if ((2020 - num) in seen):
                return num * (2020 - num)
            else:
                seen.append(num)

def day1_2(): #change so not brute force
    seen = []
    with open("day1.txt") as file:
        for line in file:
            num = int(line)
            seen.append(num)
    print(seen)
    for i in range(0, len(seen)):
        for j in range(1, len(seen)):
            for k in range(2, len(seen)):
                if (seen[i] + seen[j] + seen[k] == 2020):
                    return(seen[i]*seen[j]*seen[k])

