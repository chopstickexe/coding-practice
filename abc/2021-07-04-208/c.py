def main():
    N, K = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    ans = [K // N for _ in range(N)]
    K = K % N
    for i in sorted(range(N), key=lambda i: a[i])[:K]:
        ans[i] += 1
    for x in ans:
        print(x)


if __name__ == "__main__":
    main()
