f = open("test/01.txt", "r")
text = f.read()


def part1(text):
    cals = text.split("\n\n")
    new_cals = []
    for cal in cals:
        new_cals.append(sum([int(i) for i in cal.split("\n")]))
    return max(new_cals)


def part2(text):
    cals = text.split("\n\n")
    new_cals = []
    for cal in cals:
        new_cals.append(sum([int(i) for i in cal.split("\n")]))
    return sum(sorted(new_cals, reverse=True)[0:3])


print(part1(text))
print(part2(text))
