def under_m(n, X, M):
    """Return if X is under or equals to M"""
    m_n = []  # Mのn進数表記（1桁の値が10を超えることがあるのでlistにする）
    while 0 < M:
        m_n = [M % n] + m_n
        M = M // n
    X = [int(x) for x in str(X)]
    if len(X) != len(m_n):
        return len(X) < len(m_n)
    else:
        for x, m in zip(X, m_n):
            if x != m:
                return x < m
    return True


def binary_search(min_value, max_value, X, M) -> int:
    """Find the largest value from min_value ~ max_value
    that satisfies under_m() == True
    """
    l = min_value
    r = max_value
    while r - l > 1:
        n = (l + r) // 2
        if under_m(n, X, M):
            # n satisfies under_m() == True
            # Search larger n
            l = n
        else:
            # n doesn't satisfy under_m() == True (n is too large)
            # Search smaller n
            r = n
    # print(f"l={l}, r={r}")
    # print(under_m(l, X, M))
    # print(under_m(r, X, M))
    if under_m(l, X, M) and not under_m(r, X, M):
        return l
    else:
        # Cannot find the value that satisfies under_m() == True
        return l - 1


def main():
    X = int(input())
    M = int(input())
    d = int(max(str(X)))
    if len(str(X)) == 1:
        if d > M:
            print(0)
            return
        else:
            print(1)
            return
    ans = binary_search(d + 1, M + 1, X, M)
    print(ans - d)


if __name__ == "__main__":
    main()
