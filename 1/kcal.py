with open("input.txt", "r") as f:
    kcal_lst = []
    current_kcal = 0
    for line in f:
        if line == "\n":
            kcal_lst.append(current_kcal)
            current_kcal = 0
        else:
            current_kcal += int(line)
    kcal_lst.sort(reverse=True)
    top_1_kcal = kcal_lst[0]
    top_3_sum = sum(kcal_lst[:3])
    print(f"""
    Solution #1: {top_1_kcal}
    Solution #2: {top_3_sum}
    """)