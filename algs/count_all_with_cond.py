if __name__ == "__main__":
    conds = [(1, 2), (2, 3)]
    combinations = [(1, 1, 2), (1, 1, 3), (1, 2, 3)]
    for comb in combinations:
        count = sum(A in comb and B in comb for A, B in conds)
    print(count)  # 2
