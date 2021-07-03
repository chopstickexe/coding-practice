def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = sum([x - 10 for x in A if x > 10])
    print(ans)


if __name__ == "__main__":
    main()
