def main():
    N = int(input())
    d = []
    for _ in range(N):
        d.append(int(input()))
    d = sorted(d, reverse=True)
    kagami_mochi = []
    for r in d:
        if len(kagami_mochi) == 0 or kagami_mochi[-1] > r:
            kagami_mochi.append(r)
    print(len(kagami_mochi))


if __name__ == "__main__":
    main()
