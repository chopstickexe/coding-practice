def main():
    X, Y = [int(x) for x in input().split()]
    if abs(X - Y) < 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
