def main():
    A, B, C = [int(x) for x in input().split()]
    if A ** 2 + B ** 2 < C ** 2:
        print("Yes")
        return
    print("No")


if __name__ == "__main__":
    main()
