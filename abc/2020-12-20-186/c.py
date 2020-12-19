bases = [8 ** 5, 8 ** 4, 8 ** 3, 8 ** 2, 8, 1]


def to_8base(x: int) -> str:
    ans = ""
    for base in bases:
        e = "0"
        if x > base:
            e = str(int(x / base))
            x = x % base
        ans += e
    return ans


def main():
    n = int(input())
    count = 0
    for x in range(1, n + 1):
        if str(7) in str(x):
            continue
        x8 = to_8base(x)
        # print(f"{x}->{x8}")
        if str(7) in x8:
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    main()
