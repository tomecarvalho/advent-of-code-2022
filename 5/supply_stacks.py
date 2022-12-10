LENGTH_BLOCKS = 3


def determine_block_len(init_pos):
    for line in init_pos[:-1]:
        line_split = line.split()
        if line_split:
            return len(line_split[0])
    return None


def move_crates(n, src_stack, dest_stack, multiple_at_once=False):
    if multiple_at_once:
        dest_stack += src_stack[-n:]
        del src_stack[-n:]
    else:
        dest_stack += [src_stack.pop() for _ in range(n)]


def solve():
    with open("input.txt", "r") as f:
        init_pos, moves = f.read().split("\n\n")
        init_pos = init_pos.splitlines()
        moves = moves.splitlines()
        block_len = determine_block_len(init_pos)

        stack_names = init_pos.pop().split()
        names_dict = {name: i for i, name in enumerate(stack_names)}
        n_stacks = len(stack_names)
        stacks_1 = [[] for _ in range(n_stacks)]
        stacks_2 = [[] for _ in range(n_stacks)]

        for line in init_pos[::-1]:
            n = block_len + 1
            blocks = tuple(block.strip() for block in (
                line[i:i+n] for i in range(0, len(line), n)))
            for i, block in enumerate(blocks):
                if block:
                    for stacks in (stacks_1, stacks_2):
                        stacks[i].append(block)

        for move in moves:
            move_split = move.split()
            n = int(move_split[1])
            src_stack_idx = names_dict[move_split[3]]
            dest_stack_idx = names_dict[move_split[5]]

            src_stack_1 = stacks_1[src_stack_idx]
            dest_stack_1 = stacks_1[dest_stack_idx]

            src_stack_2 = stacks_2[src_stack_idx]
            dest_stack_2 = stacks_2[dest_stack_idx]

            move_crates(n, src_stack_1, dest_stack_1)
            move_crates(n, src_stack_2, dest_stack_2, True)

        def stacks_on_top_str(stacks):
            return "".join(stack[-1][1] if stack else " " for stack in stacks)

        for i, stacks in enumerate((stacks_1, stacks_2), 1):
            print(f"Solution #{i}: {stacks_on_top_str(stacks)}")


solve()
