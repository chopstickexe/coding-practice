def main():
    X = [int(x) for x in input()]
    if all([X[i] == X[i - 1] for i in range(1, 4)]) or all(
        X[i + 1] == X[i] + 1 or (X[i + 1] == 0 and X[i] == 9) for i in range(0, 3)
    ):
        print("Weak")
    else:
        print("Strong")


if __name__ == "__main__":
    main()
