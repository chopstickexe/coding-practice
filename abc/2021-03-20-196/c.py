from itertools import product


def main():
    N = input()
    ans = 0
    for d in range(2, len(N)):
        if d % 2 != 0:
            continue
        ans += 9 * (10 ** (d // 2 - 1))
    # print(ans)
    if len(N) % 2 != 0:
        # Finish if the number of digits is odd
        print(ans)
        return
    half_digit = len(N) // 2
    for x in product(range(0, 10), repeat=half_digit):
        # Count numbers having the same number of digits
        if x[0] == 0:
            continue
        x = int("".join(map(str, x)))
        if x > int(N[0:half_digit]):
            continue
        elif x < int(N[0:half_digit]):
            ans += 1
        elif x == int(N[0:half_digit]) and x <= int(N[half_digit:]):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
