f = open("test/03.txt", "r")
text = f.read()


def part1(text):
    sacks = text.split("\n")
    priorities = []
    for sack in sacks:
        first, second = set(sack[0 : len(sack) // 2]), set(sack[len(sack) // 2 :])
        letter = first.intersection(second).pop()
        if ord(letter) >= 97:
            priorities.append(ord(letter) - ord("a") + 1)
        else:
            priorities.append(ord(letter) - ord("A") + 26 + 1)
    return sum(priorities)


def part2(text):
    sacks = text.split("\n")
    priorities = []
    for index in range(0, len(sacks), 3):
        one, two, three = (
            set(sacks[index]),
            set(sacks[index + 1]),
            set(sacks[index + 2]),
        )
        letter = one.intersection(two).intersection(three).pop()
        if ord(letter) >= 97:
            priorities.append(ord(letter) - ord("a") + 1)
        else:
            priorities.append(ord(letter) - ord("A") + 26 + 1)
    return sum(priorities)


print(part1(text))
print(part2(text))
