def main():
    A, B, K = [int(x) for x in input().split()]
    A -= K
    if A < 0:
        B += A
        A = 0
    if B < 0:
        B = 0
    print(f"{A} {B}")


if __name__ == "__main__":
    main()
