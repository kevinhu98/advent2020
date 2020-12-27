player1Hand = []
player2Hand = []

p1Hand = True  # while P1 hand true, add cards to p1 hand else add to p2 hand
with open("day22.txt") as file:
    next(file)
    for line in file:
        if line != "\n":
            if p1Hand:
                player1Hand.append(int(line))
            else:
                player2Hand.append(int(line))
        else:
            p1Hand = False
            next(file)

while player1Hand and player2Hand:
    print(player1Hand, player2Hand)
    if player1Hand[0] > player2Hand[0]:  # if p1 card better, add card to end and taken card
        winningCard = player1Hand[0]
        transferredCard = player2Hand[0]
        del player2Hand[0]
        del player1Hand[0]
        player1Hand.append(winningCard)
        player1Hand.append(transferredCard)
    else:
        winningCard = player2Hand[0]
        transferredCard = player1Hand[0]
        del player2Hand[0]
        del player1Hand[0]
        player2Hand.append(winningCard)
        player2Hand.append(transferredCard)

score = 0
count = max(len(player1Hand), len(player2Hand))
if player1Hand:
    for card in player1Hand:
        score += (count * card)
        count -= 1
else:
    for card in player2Hand:
        score += (count * card)
        count -= 1

print(score)
