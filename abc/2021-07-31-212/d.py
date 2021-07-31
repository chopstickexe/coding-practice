import heapq


def main():
    Q = int(input())
    h = []
    add_x = 0
    for _ in range(0, Q):
        query = [int(x) for x in input().split()]
        if query[0] == 3:
            print(heapq.heappop(h) + add_x)
        elif query[0] == 1:
            query[1] -= add_x
            heapq.heappush(h, query[1])
        elif query[0] == 2:
            add_x += query[1]


if __name__ == "__main__":
    main()
