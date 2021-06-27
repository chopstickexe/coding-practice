def main():
    abcs = [int(x) for x in input().split()]
    abcs.sort(reverse=True)
    print(abcs[0] + abcs[1])


if __name__ == "__main__":
    main()
