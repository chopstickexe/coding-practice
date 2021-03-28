from itertools import product

def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    ans = -1
    for p in product([True, False], repeat=N):
        ors = []
        v = 0
        for i, a in enumerate(A):
            if p[i] == True:
                ors.append(v)
                v = 0
            v = v | a
        ors.append(v)
        xor = 0
        for v in ors:
            xor = xor ^ v
        if ans == -1 or xor < ans:
            ans = xor
    print(ans)


if __name__ == "__main__":
    main()
