def main():
    N = int(input())
    points = [(0, 0, 0)]
    for _ in range(N):
        t, x, y = [int(x) for x in input().split()]
        points.append((t, x, y))
    ans = True
    for i in range(1, N + 1):
        t1, x1, y1 = points[i - 1]
        t2, x2, y2 = points[i]
        dt = t2 - t1
        d = abs(x2 - x1) + abs(y2 - y1)
        if d > dt or (dt - d) % 2 == 1:
            # Cannot go
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
