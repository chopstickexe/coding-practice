def main():
    A, B, C = [int(x) for x in input().split()]
    if A < 0 and C % 2 == 0:
        A = -A
    if B < 0 and C % 2 == 0:
        B = -B

    if A > B:
        print(">")
        return
    elif A == B:
        print("=")
        return
    print("<")


if __name__ == "__main__":
    main()
