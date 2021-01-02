def main():
    A, B = [str(x) for x in input().split()]
    sum_a = int(A[0]) + int(A[1]) + int(A[2])
    sum_b = int(B[0]) + int(B[1]) + int(B[2])
    if sum_a > sum_b:
        print(sum_a)
    else:
        print(sum_b)


if __name__ == "__main__":
    main()
