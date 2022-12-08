def contains(pair):
    (x0, y0), (x1, y1) = pair
    return (x0 <= x1 and y0 >= y1) or (x1 <= x0 and y1 >= y0)


def overlaps(pair):
    (x0, y0), (x1, y1) = pair
    if x0 <= x1 and y0 <= y1:
        return not y0 < x1
    else:
        return not y1 < x0


with open("input.txt", "r") as f:
    pairs = [line.split(",") for line in f.read().splitlines()]
    pairs_int = []
    for pair in pairs:
        pair_int = []
        for el in pair:
            n1, n2 = el.split("-")
            pair_int.append((int(n1), int(n2)))
        pairs_int.append(pair_int)
    count_contains = sum(contains(pair) for pair in pairs_int)
    count_overlaps = sum(overlaps(pair) for pair in pairs_int)
    print(f"Solution #1: {count_contains}")
    print(f"Solution #2: {count_overlaps}")
