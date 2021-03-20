import math


def main():
    A, B, W = [int(x) for x in input().split()]
    W *= 1000
    ans = []
    for x in range(1, math.floor(W / A) + 1):
        res = W - A * x
        if res > (B - A) * x:
            continue
        ans.append(x)
    # print(ans)
    if len(ans) == 0:
        print("UNSATISFIABLE")
        return
    print(f"{ans[0]} {ans[-1]}")


if __name__ == "__main__":
    main()
