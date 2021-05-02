def main():
    N = int(input())
    S = list(input())
    Q = int(input())

    count = 0
    for _ in range(Q):
        T, A, B = [int(x) for x in input().split()]
        if T == 2:
            count += 1
        else:  # T == 1
            if count % 2 == 0:
                # Not switched
                i = A - 1
                j = B - 1
            else:
                # Switched
                i = N + A - 1 if A <= N else A - N - 1
                j = N + B - 1 if B <= N else B - N - 1
            tmp = S[i]
            S[i] = S[j]
            S[j] = tmp
    if count % 2 == 1:
        S = S[N:] + S[:N]
    print("".join(S))


if __name__ == "__main__":
    main()
