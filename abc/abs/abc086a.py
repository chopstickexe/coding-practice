def main():
    a, b = [int(x) for x in input().split()]
    ans = "Odd" if a * b % 2 == 1 else "Even"
    print(ans)


if __name__ == "__main__":
    main()
