f = open("test/02.txt", "r")
text = f.read()

opp_play = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

you_play = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

you_want = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

lose = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

win = {
    "scissors": "rock",
    "rock": "paper",
    "paper": "scissors"
}

def part1(text):
    rounds = text.split("\n")
    round_arr = []
    for round in rounds:
        opponent, yours = round.split(" ")
        opp, you = opp_play[opponent], you_play[yours]
        outcome = 0
        if you == "rock" and opp == "scissors":
            outcome = 6
        elif you == "paper" and opp == "rock":
            outcome = 6
        elif you == "scissors" and opp == "paper":
            outcome = 6
        elif you == opp:
            outcome = 3
        else:
            outcome = 0
        shape = 0
        if you == "rock":
            shape = 1
        elif you == "paper":
            shape = 2
        else:
            shape = 3
        round_arr.append(outcome + shape)
    return sum(round_arr)

def part2(text):
    rounds = text.split("\n")
    round_arr = []
    for round in rounds:
        opponent, yours = round.split(" ")
        opp, want = opp_play[opponent], you_want[yours]
        outcome = 0
        if want == "win":
            you = win[opp]
            outcome = 6
        elif want == "lose":
            you = lose[opp]
            outcome = 0
        elif want == "draw":
            you = opp
            outcome = 3
        shape = 0
        if you == "rock":
            shape = 1
        elif you == "paper":
            shape = 2
        else:
            shape = 3
        print(opp, want, you, outcome + shape)
        round_arr.append(outcome + shape)
    return sum(round_arr)


print(part1(text))
print(part2(text))
