import itertools


def main():
    N, M = [int(x) for x in input().split()]
    conds = [(int(A), int(B)) for A, B in [input().split() for _ in range(M)]]
    # print("***")
    # print(conds)

    K = int(input())
    choices = [(int(C), int(D)) for C, D in [input().split() for _ in range(K)]]
    # print("***")
    # print(choices)

    ans = 0
    for balls in itertools.product(*choices):  # for all combinations of items in tuples
        # print("***")
        # print(balls)
        balls = set(balls)
        count = sum(A in balls and B in balls for A, B in conds)
        if ans < count:
            ans = count

    print(ans)


if __name__ == "__main__":
    main()
