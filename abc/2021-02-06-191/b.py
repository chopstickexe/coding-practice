def main():
    N, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    ans = []
    for a in A:
        if a == X:
            continue
        ans.append(str(a))
    if len(ans) == 0:
        print('')
    else:
        print(' '.join(ans))


if __name__ == "__main__":
    main()
