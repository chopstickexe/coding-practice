def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            for k in range(j + 1, n):
                xk, yk = points[k]
                if xi == xj or xi == xk:
                    if xi == xj == xk:
                        print(f"Yes")
                        return
                    else:
                        continue  # avoid div 0
                if yi == yj or yi == yk:
                    if yi == yj == yk:
                        print(f"Yes")
                        return
                    else:
                        continue  # avoid div 0
                if (xj - xi) / (yj - yi) == (xk - xi) / (yk - yi):
                    print(f"Yes")
                    return
    print("No")

if __name__ == "__main__":
    main()