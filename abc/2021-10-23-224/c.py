def _is_triangle(p1, p2, p3):
    """Returns False if the 3 points consist a line, True otherwise"""
    if p1[0] == p2[0] == p3[0] or p1[1] == p2[1] == p3[1]:
        return False
    if (p2[0] != p1[0]) and (
        (p3[1] - p1[1]) == ((p2[1] - p1[1]) / (p2[0] - p1[0])) * (p3[0] - p1[0])
    ):  # p3 is on the line of p1-p3
        return False
    return True


def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = [int(x) for x in input().split()]
        points.append((x, y))

    ans = 0
    for i in range(N):
        p1 = points[i]
        for j in range(i + 1, N):
            p2 = points[j]
            for k in range(j + 1, N):
                p3 = points[k]
                if _is_triangle(p1, p2, p3):
                    ans += 1
    print(ans)


if __name__ == "__main__":
    main()
