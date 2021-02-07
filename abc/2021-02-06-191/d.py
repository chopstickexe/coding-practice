import math


def main():
    X, Y, R = [int(float(x) * 10000) for x in input().split()]
    # Find integers x & y that satisfy the conditions
    count = 0
    x_min = math.ceil((X - R) / 10000)
    x_max = math.floor((X + R) / 10000) + 1
    for x in range(x_min, x_max):
        x *= 10000
        temp = R ** 2 - (x - X) ** 2
        if temp < 0:
            continue
        temp = math.sqrt(temp)
        min_y = math.ceil((Y - temp) / 10000)
        max_y = math.floor((Y + temp) / 10000)
        # print(f"x={x // 10000}, max_y={max_y}, min_y={min_y}")
        count += (max_y - min_y + 1)
    print(count)


if __name__ == "__main__":
    main()
