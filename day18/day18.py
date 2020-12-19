def evaluate(equation: str) -> int:  # first simplify and remove parens, then left to right
    chars = [char for char in equation.strip() if char !=" "]

    while "(" in chars:  # once out of loop, should be no more parens

        for i in range(len(chars)):
            if chars[i] == "(":
                leftParens = i
            if chars[i] == ")":
                rightParens = i
                break
        total = int(chars[leftParens + 1])  # starts at the number to the right of parentheses
        for i in range(leftParens + 2, rightParens-1):  # starts at the first symbol in parentheses

            if chars[i] == "*":
                total *= int(chars[i + 1])
            elif chars[i] == "+":  # must be addition symbol
                total += int(chars[i + 1])

        chars[leftParens] = total  # replace everything between two parens with total
        del chars[leftParens+1: rightParens+1]

    sum = int(chars[0])

    for i in range(1, len(chars) - 1):
        if chars[i] == "*":
            sum *= int(chars[i + 1])
        elif chars[i] == "+":  # must be addition symbol
            sum += int(chars[i + 1])

    return sum
def day18_1(inputFile):
    sum = 0
    with open(inputFile) as f:
        lines = [line.strip() for line in f]
    for line in lines:
        sum += evaluate(line)
    return sum

print(day18_1("day18.txt"))
