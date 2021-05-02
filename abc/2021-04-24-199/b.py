def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    min_x = A[0]
    max_x = B[0]
    for i in range(1, N):
        if min_x < A[i]:
            min_x = A[i]
        if B[i] < max_x:
            max_x = B[i]
    ans = max_x - min_x + 1
    print(ans if ans >= 0 else 0)


if __name__ == "__main__":
    main()
