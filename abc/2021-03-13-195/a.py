def main():
    M, H = [int(x) for x in input().split()]
    if H % M == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
