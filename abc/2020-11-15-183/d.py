from dataclasses import dataclass


@dataclass
class Event:
    time: int
    use: int  # Negative if someone stop using the water


def main():
    N, W = [int(x) for x in input().split()]
    events = []
    for n in range(0, N):
        S, T, P = [int(x) for x in input().split()]
        events.append(Event(S, P))
        events.append(Event(T, -P))
    events.sort(key=lambda e: (e.time, e.use))
    # print(events)
    use = 0
    for e in events:
        use += e.use
        if use > W:
            # Since events are sorted by time and use, negative use comes earlier than positive at the same time
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
