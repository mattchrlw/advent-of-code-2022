f = open("test/06.txt", "r")
text = f.read()


def part1(text):
    idx = 0
    for i in range(len(text) - 4):
        if len(set(text[i-4:i])) == 4:
            return idx
        idx += 1

def part2(text):
    idx = 0
    for i in range(len(text) - 14):
        if len(set(text[i-14:i])) == 14:
            return idx
        idx += 1


print(part1(text))
print(part2(text))
