def main():
    S = input()
    ans = True
    for i in range(len(S)):
        if (i + 1) % 2 != 0 and not S[i].islower():
            # print(S[i])
            ans = False
            break
        elif (i + 1) % 2 == 0 and not S[i].isupper():
            # print(S[i])
            ans = False
            break
    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
