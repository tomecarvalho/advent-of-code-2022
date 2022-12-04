INPUT = "input.txt"
MODE = "r"

diff_a = ord('a') - 1
diff_A = ord('A') - 27


def char_priority(char):
    return ord(char) - (diff_a if char.islower() else diff_A)


def solve_1():
    with open(INPUT, MODE) as f:
        rucksacks = f.read().splitlines()
        priorities_sum = 0
        for rucksack in rucksacks:
            middle = int(len(rucksack) / 2)
            compartments = (set(rucksack[:middle]), set(rucksack[middle:]))
            char_intersections = compartments[0].intersection(compartments[1])
            priorities_sum += sum(char_priority(char)
                                  for char in char_intersections)
        return priorities_sum


def solve_2():
    with open(INPUT, MODE) as f:
        priorities_sum = 0
        groups = [[]]

        group_lines_read = 0
        for line in f.readlines():
            if group_lines_read == 3:
                groups.append([line.strip()])
                group_lines_read = 1
            else:
                groups[-1].append(line.strip())
                group_lines_read += 1
        
        for rucksacks in groups:
            common_items = set(rucksacks[0])
            for rucksack in rucksacks[1:]:
                common_items = common_items.intersection(set(rucksack))
            priorities_sum += sum(char_priority(char) for char in common_items)
            
        return priorities_sum


print(f"Solution #1: {solve_1()}")
print(f"Solution #2: {solve_2()}")