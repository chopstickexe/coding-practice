from decimal import Decimal
import math


def main():
    # Ref: https://atcoder.jp/contests/abc191/submissions/20025185
    X, Y, R = [Decimal(x) for x in input().split()]
    # Find integers x & y that satisfy the conditions
    count = 0
    x_min = math.ceil(X - R)
    x_max = math.floor(X + R) + 1
    for x in range(x_min, x_max):
        temp = (R ** 2 - (x - X) ** 2).sqrt()
        min_y = math.ceil(Y - temp)
        max_y = math.floor(Y + temp)
        # print(f"x={x // 10000}, max_y={max_y}, min_y={min_y}")
        count += (max_y - min_y + 1)
    print(count)


if __name__ == "__main__":
    main()
