def main():
    N, S, D = [int(x) for x in input().split()]
    ans = False
    for i in range(N):
        X, Y = [int(x) for x in input().split()]
        if X < S and Y > D:
            ans = True
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
