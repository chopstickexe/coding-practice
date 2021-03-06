def main():
    A, B = [int(x) for x in input().split()]
    nyu_kokei = A + B
    nyu_shibou = B
    if nyu_kokei >= 15 and nyu_shibou >= 8:
        print(1)
    elif nyu_kokei >= 10 and nyu_shibou >= 3:
        print(2)
    elif nyu_kokei >= 3:
        print(3)
    else:
        print(4)


if __name__ == "__main__":
    main()
