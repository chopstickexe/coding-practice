def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    A.sort()
    B.sort()

    i = 0
    j = 0

    ans = 10 ** 9 - 1

    while i < N and j < M:
        x = abs(A[i] - B[j])
        if x < ans:
            ans = x
        if A[i] < B[j]:
            # put A
            i += 1
        else:
            j += 1

    print(ans)


if __name__ == "__main__":
    main()
