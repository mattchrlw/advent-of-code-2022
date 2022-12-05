f = open("test/05.txt", "r")
text = f.read()


def part1(text):
    crs, ms = text.split("\n\n")
    cs = crs.split("\n")
    cs_idx = int(cs[len(cs) - 1].split(" ")[-2])
    # print(cs_idx)
    crates = {}
    for i in range(1, cs_idx + 1):
        crates[i] = []
    for c in cs:
        if c[1] != '1':
            vals = [c[i] for i in range(1, len(c), 4)]
            for idx, v in enumerate(vals):
                if v != ' ':
                    crates[idx+1].append(v)
            # print(vals)
    # print(crates)

    moves = ms.split("\n")
    for move in moves:
        num, rest = move[5:].split(" from ")
        start, end = rest.split(" to ")
        num, start, end = int(num), int(start), int(end)
        for _ in range(num):
            moving = crates[start].pop(0)
            crates[end].insert(0, moving)
    final_str = ""
    for c in crates.values():
        final_str += c[0]
    return final_str

def part2(text):
    crs, ms = text.split("\n\n")
    cs = crs.split("\n")
    cs_idx = int(cs[len(cs) - 1].split(" ")[-2])
    # print(cs_idx)
    crates = {}
    for i in range(1, cs_idx + 1):
        crates[i] = []
    for c in cs:
        if c[1] != '1':
            vals = [c[i] for i in range(1, len(c), 4)]
            for idx, v in enumerate(vals):
                if v != ' ':
                    crates[idx+1].append(v)
            # print(vals)
    # print(crates)

    moves = ms.split("\n")
    for move in moves:
        num, rest = move[5:].split(" from ")
        start, end = rest.split(" to ")
        num, start, end = int(num), int(start), int(end)
        moving = crates[start][0:num]
        crates[start] = crates[start][num:]
        for m in reversed(moving):
            crates[end].insert(0, m)
    final_str = ""
    for c in crates.values():
        final_str += c[0]
    return final_str


print(part1(text))
print(part2(text))
