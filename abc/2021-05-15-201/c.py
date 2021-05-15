import itertools


def main():
    S = input()
    numbers = []
    must = [False for _ in range(10)]
    for i, s in enumerate(S):
        if s == "o":
            numbers.append(i)
            must[i] = True
        elif s == "?":
            numbers.append(i)
    ans = 0
    for nums in itertools.product(numbers, repeat=4):
        check = must.copy()
        for n in nums:
            if check[n]:
                check[n] = False
        if sum(check) == 0:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
