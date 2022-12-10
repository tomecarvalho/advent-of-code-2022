LENGTH_BLOCKS = 3


def determine_block_len(init_pos):
    for line in init_pos[:-1]:
        line_split = line.split()
        if line_split:
            return len(line_split[0])
    return None


with open("input.txt", "r") as f:
    init_pos, moves = f.read().split("\n\n")
    init_pos = init_pos.splitlines()
    moves = moves.splitlines()
    block_len = determine_block_len(init_pos)

    stack_names = init_pos.pop().split()
    names_dict = {name: i for i, name in enumerate(stack_names)}
    n_stacks = len(stack_names)
    stacks = [[] for _ in range(n_stacks)]

    for line in init_pos[::-1]:
        n = block_len + 1
        blocks = tuple(block.strip() for block in (
            line[i:i+n] for i in range(0, len(line), n)))
        for i, block in enumerate(blocks):
            if block:
                stacks[i].append(block)

    for move in moves:
        move_split = move.split()
        n = int(move_split[1])
        src_stack = stacks[names_dict[move_split[3]]]
        dest_stack = stacks[names_dict[move_split[5]]]
        dest_stack += [src_stack.pop() for _ in range(n)]

    print(f"Solution #1: '{''.join(stack[-1][1] if stack else ' ' for stack in stacks)}'")