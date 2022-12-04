f = open("test/04.txt", "r")
text = f.read()


def part1(text):
    pairs = text.split("\n")
    full_contain = 0
    for pair in pairs:
        range_1, range_2 = pair.split(",")
        range_1_start, range_1_end = range_1.split("-")
        range_2_start, range_2_end = range_2.split("-")
        act_range_1, act_range_2 = set(range(int(range_1_start), int(range_1_end)+1)), set(range(int(range_2_start), int(range_2_end)+1))
        if act_range_1.intersection(act_range_2) == act_range_1 or act_range_2.intersection(act_range_1) == act_range_2:
            full_contain += 1
    return full_contain


def part2(text):
    pairs = text.split("\n")
    full_contain = 0
    for pair in pairs:
        range_1, range_2 = pair.split(",")
        range_1_start, range_1_end = range_1.split("-")
        range_2_start, range_2_end = range_2.split("-")
        act_range_1, act_range_2 = set(range(int(range_1_start), int(range_1_end)+1)), set(range(int(range_2_start), int(range_2_end)+1))
        if act_range_1.intersection(act_range_2) != set() or act_range_2.intersection(act_range_1) != set():
            full_contain += 1
    return full_contain


print(part1(text))
print(part2(text))
