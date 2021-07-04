def main():
    A, B = [int(x) for x in input().split()]
    if 1 * A <= B and B <= 6 * A:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
