S = []
memo_t = []
memo_f = []


def find(k, flag):
    if k == 0:
        return 1
    elif flag and memo_t[k] > 0:
        return memo_t[k]
    elif not flag and memo_f[k] > 0:
        return memo_f[k]

    op = S[k - 1]
    if op == "AND":
        if flag:
            memo_t[k] = find(k - 1, True)
            return memo_t[k]
        else:
            memo_f[k] = find(k - 1, False) * 2 + find(k - 1, True)
            return memo_f[k]
    else:
        if flag:
            memo_t[k] = find(k - 1, True) * 2 + find(k - 1, False)
            return memo_t[k]
        else:
            memo_f[k] = find(k - 1, False)
            return memo_f[k]


def main():
    N = int(input())
    global S, memo_t, memo_f
    for _ in range(N):
        S.append(input())
    # memo the result of find
    memo_t = [0 for _ in range(N + 1)]
    memo_f = [0 for _ in range(N + 1)]
    print(find(N, True))


if __name__ == "__main__":
    main()
