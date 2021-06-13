# (a + b) mod n = ((a mod n) + b) mod n
# Max loop numbers: K (variation of mod value)


def main():
    K = int(input())
    for i in range(K + 1):
        if i == 0:
            x = 7
        else:
            x = 10 * x + 7
        x = x % K
        if x == 0:
            print(i + 1)
            return
    print(-1)


if __name__ == "__main__":
    main()
