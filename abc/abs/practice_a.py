def main():
    a = int(input())
    b, c = [int(x) for x in input().split()]
    s = input()
    print(f"{a+b+c} {s}")


if __name__ == "__main__":
    main()
