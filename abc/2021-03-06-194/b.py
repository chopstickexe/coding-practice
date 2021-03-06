def main():
    N = int(input())
    employees = []
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        employees.append((i, A, B))
    ans = 2 * (10 ** 5)
    for i in range(N):
        ei = employees[i]
        A = ei[1]
        for j in range(N):
            ej = employees[j]
            B = ej[2]
            if i == j and A + B < ans:
                ans = A + B
            elif i != j and max(A, B) < ans:
                ans = max(A, B)
    print(ans)


if __name__ == "__main__":
    main()
