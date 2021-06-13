import bisect


def main():
    N, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]  # Already sorted
    K = []
    for _ in range(Q):
        K.append(int(input()))
    x = {}  # key = index, value = starting number
    index = 1
    for i, a in enumerate(A):
        if i == 0:
            if a == 1:
                # no missing numbers before A[0]
                continue
            else:
                start = 1
        else:
            start = A[i - 1] + 1
        skipped = a - start
        if skipped == 0:
            continue
        x[index] = start
        index += skipped
    start = A[-1] + 1
    x[index] = A[-1] + 1

    keys = sorted(list(x.keys()))
    for k in K:
        key_index = bisect.bisect(keys, k)  # returns index to insert k
        key = keys[key_index - 1]
        val = x[key]
        if key == k:
            print(val)
        else:
            print(val + (k - key))


if __name__ == "__main__":
    main()
