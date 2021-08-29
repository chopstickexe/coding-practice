import math


def main():
    N = int(input())
    ans_stack = []

    while N > 1:
        res = N % 2
        if res == 1:
            ans_stack.append("A")
        ans_stack.append("B")
        N //= 2
    ans_stack.append("A")

    print(''.join(ans_stack[::-1]))


if __name__ == "__main__":
    main()
