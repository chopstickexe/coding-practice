def _is_triangle(p1, p2, p3):
    """Returns True if area of the triangle is larger than 0, False otherwise"""
    if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]) == 0:
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
