def checkValid(preamble: [int], sum: int) -> bool:  # check if two numbers add up to sum (basically 2sum)
    seen = []
    for num in preamble:
        if (sum - num) in seen:
            return True
        else:
            seen.append(num)
    return False

def day9_1(inputFile):
    preambleLength = 25  # how many previous numbers
    nums = []

    with open(inputFile) as file:  # put all nums into list
        for line in file:
            nums.append(int(line.strip()))
    file.close()

    for i in range(preambleLength, len(nums)):
        if not checkValid(nums[i-preambleLength:i], nums[i]):
            return nums[i]

def day9_2(inputFile):
    # same as pt 1 but store value in invalid
    preambleLength = 25  # how many previous numbers
    nums = []

    with open(inputFile) as file:  # put all nums into list
        for line in file:
            nums.append(int(line.strip()))
    file.close()

    for i in range(preambleLength, len(nums)):
        if not checkValid(nums[i - preambleLength:i], nums[i]):
            invalid = nums[i]
            break

    # new code starts here
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if sum(nums[i:j]) == invalid:
                return min(nums[i:j]) + max(nums[i:j])

#2399181
if __name__ == "__main__":
    print(day9_2("day9.txt"))