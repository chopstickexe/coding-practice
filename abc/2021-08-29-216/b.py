from collections import defaultdict


def main():
    N = int(input())
    names = defaultdict(set)
    ans = False
    for _ in range(N):
        S, T = input().split()
        if S in names.keys() and T in names[S]:
            ans = True
    print("Yes") if ans else print("No")


if __name__ == "__main__":
    main()
