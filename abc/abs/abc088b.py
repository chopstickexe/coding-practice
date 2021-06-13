def main():
    _ = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, reverse=True)
    alice = sum([x for i, x in enumerate(a) if i % 2 == 0])
    bob = sum([x for i, x in enumerate(a) if i % 2 == 1])
    print(alice - bob)


if __name__ == "__main__":
    main()
