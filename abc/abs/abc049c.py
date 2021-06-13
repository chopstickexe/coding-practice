from collections import deque


def main():
    S = input()
    Ts = deque()
    elms = ["dream", "dreamer", "erase", "eraser"]
    for e in elms:
        if S[:len(e)] == e:
            Ts.append(e)
    found = False
    while len(Ts) > 0 and not found:
        T = Ts.popleft()
        current = len(T)
        for e in elms:
            if S[current:len(e) + current] != e:
                # Doesn't matche with S, ignore
                continue
            NEW_T = T + e
            if len(S) == len(NEW_T):
                found = True
                break
            else:
                Ts.append(NEW_T)
    if found:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
