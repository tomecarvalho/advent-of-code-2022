def unique(lst):
    return len(set(lst)) == len(lst)


def find_1st_n_distinct_chars(data, n):
    for i in range(len(data) - n + 1):
        if unique(data[i:i + n]):
            return i + n


def solve():
    with open("input.txt", "r") as f:
        data = f.read()
        for i, n in enumerate((4, 14), 1):
            print(f"Solution #{i}: {find_1st_n_distinct_chars(data, n)}")


solve()
