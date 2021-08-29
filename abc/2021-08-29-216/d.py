from collections import defaultdict, deque


def main():
    N, M = [int(x) for x in input().split()]
    bins = [0 for _ in range(M)]
    balls = [[] for _ in range(M)]
    tops = defaultdict(list)
    for i in range(M):
        bins[i] = int(input())
        balls[i] = deque([int(x) for x in input().split()])
        tops[balls[i][0]].append(i)
    twins = deque([c for c, v in tops.items() if len(v) == 2])
    
    while len(twins) > 0:
        c = twins.popleft()
        selected = tops.pop(c)
        for i in selected:
            balls[i].popleft()
            if len(balls[i]) > 0:
                next_c = balls[i][0]
                tops[next_c].append(i)
                if len(tops[next_c]) == 2:
                    twins.append(next_c)
    if len(tops) > 0:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
