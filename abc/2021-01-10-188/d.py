from collections import defaultdict


def main():
    N, C = [int(x) for x in input().split()]
    spends = defaultdict(int)
    for i in range(N):
        a, b, c = [int(x) for x in input().split()]
        start = a - 1
        end = b
        spends[start] += c
        spends[end] -= c
    # print(spends)
    days = sorted(spends.keys())
    total = 0
    current = 0  # Current spend if not using prime
    for i, d in enumerate(days):
        current += spends[d]
        # print(f"day{d} current spend per day (without prime) = {current}")
        spend_per_day = current
        if spend_per_day > C:
            # Use prime
            spend_per_day = C
        next_d = d + 1
        if i + 1 < len(days):
            next_d = days[i + 1]
        total += spend_per_day * (next_d - d)
        # print(f"day{next_d} total = {total}")
    print(total)


if __name__ == "__main__":
    main()
