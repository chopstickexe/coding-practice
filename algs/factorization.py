# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

def factorization(n: int):
    """nの素因数分解を行うコード。nの素因数の最大値は高々ルートn、という性質を用いた試し割り法(O(route(n)))
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


if __name__ == "__main__":
    print(factorization(24))  # [[2, 3], [3, 1]] (=2x2x2x3)

