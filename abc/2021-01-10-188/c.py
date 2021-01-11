import queue


def main():
    # MAX N = 16
    # MAX 2^N = 2^16 = 65536
    N = int(input())
    A = [int(x) for x in input().split()]
    q = queue.Queue()
    [q.put(i) for i in range(2 ** N)]
    while not q.empty():
        i = q.get()
        j = q.get()
        if q.qsize() > 0:
            win = i if A[i] > A[j] else j
            q.put(win)
            # print(f"win={win}")
        else:
            print(i + 1 if A[i] < A[j] else j + 1)
            break


if __name__ == "__main__":
    main()
