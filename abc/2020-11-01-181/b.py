def main():
    n = int(input())
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    for i in range(n):
        a_str, b_str = input().split()
        a[i] = int(a_str)
        b[i] = int(b_str)
    sum = 0
    for i in range(n):
        assert b[i] >= a[i]
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    print(sum)

if __name__ == "__main__":
    main()