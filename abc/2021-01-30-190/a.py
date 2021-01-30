def main():
    A, B, C = [int(x) for x in input().split()]
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
