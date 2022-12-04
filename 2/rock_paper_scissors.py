INPUT = "input.txt"
MODE = "r"

ROCK = "R"
PAPER = "P"
SCISSORS = "S"

LOSS = "L"
DRAW = "D"
WIN = "W"

beats = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

loses_to = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

scores = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

opponent_moves = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

our_moves = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

our_desired_results = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN,
}

outcome_scores = {
    LOSS: 0,
    DRAW: 3,
    WIN: 6,
}


def calc_score(opponent_move, our_move):
    if our_move == opponent_move:
        outcome_score = outcome_scores[DRAW]
    elif beats[our_move] == opponent_move:
        outcome_score = outcome_scores[WIN]
    else:
        outcome_score = outcome_scores[LOSS]
    return scores[our_move] + outcome_score


def solve_1():
    with open(INPUT, MODE) as f:
        score = 0
        for line in f:
            opponent_move_abc, our_move_xyz = line.strip().split()
            opponent_move = opponent_moves[opponent_move_abc]
            our_move = our_moves[our_move_xyz]
            score += calc_score(opponent_move, our_move)
        return score


def solve_2():
    def choose_move(opponent_move, desired_res):
        if desired_res == LOSS:
            return beats[opponent_move]
        elif desired_res == DRAW:
            return opponent_move
        else:
            return loses_to[opponent_move]

    with open(INPUT, MODE) as f:
        score = 0
        for line in f:
            opponent_move_abc, our_desired_res_xyz = line.strip().split()
            opponent_move = opponent_moves[opponent_move_abc]
            desired_res = our_desired_results[our_desired_res_xyz]
            our_move = choose_move(opponent_move, desired_res)
            score += calc_score(opponent_move, our_move)
        return score

print(f"Solution #1: {solve_1()}")
print(f"Solution #2: {solve_2()}")
