def main():
    N, M = [int(x) for x in input().split()]
    conds = []
    for i in range(M):
        A, B = [int(x) for x in input().split()]
        conds.append((A, B))
    # print(conds)
    # print("***")
    K = int(input())
    choices = []
    for i in range(K):
        C, D = [int(x) for x in input().split()]
        choices.append((C, D))

    ans = 0
    for x in range(2 ** K):
        # 2 ** 16 == 65536
        selection = set()
        for i, c in enumerate(f"{x:b}".zfill(K)):
            dish = choices[i][int(c)]
            selection.add(dish)
        matched = 0
        for i in range(M):
            if all([d in selection for d in conds[i]]):
                matched += 1
                # print(f"matched: condition = {conds[i]}, selection = {selection}")
        if matched > ans:
            ans = matched
    print(ans)


if __name__ == "__main__":
    main()
