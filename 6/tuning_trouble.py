def unique(lst):
    return len(set(lst)) == len(lst)


def solve_1():
    with open("input.txt", "r") as f:
        data = f.read()
        for i in range(len(data) - 3):
            chars = data[i:i + 4]
            if unique(chars):
                return i + 4


print(f"Solution #1: {solve_1()}")
