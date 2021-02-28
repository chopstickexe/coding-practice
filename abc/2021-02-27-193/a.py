def main():
    A, B = [int(x) for x in input().split()]
    A *= 100
    B *= 100
    print((A - B) / A * 100)


if __name__ == "__main__":
    main()
