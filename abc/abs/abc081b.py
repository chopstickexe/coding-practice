def main():
    _ = int(input())
    A = [int(x) for x in input().split()]
    find_odd = False
    ans = 0
    while not find_odd:
        for i, a in enumerate(A):
            if a % 2 == 1:
                find_odd = True
                break
            A[i] = a // 2
        if not find_odd:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
