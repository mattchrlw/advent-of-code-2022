f = open("test/06.txt", "r")
text = f.read()


def part1(text):
    for i in range(len(text) - 4):
        if len(set(text[i-4:i])) == 4:
            return i

def part2(text):
    for i in range(len(text) - 14):
        if len(set(text[i-14:i])) == 14:
            return i


print(part1(text))
print(part2(text))
