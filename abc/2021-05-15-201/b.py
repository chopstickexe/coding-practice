def main():
    N = int(input())
    mountains = []
    for _ in range(N):
        S, T = input().split()
        mountains.append((int(T), S))
    mountains = sorted(mountains, reverse=True)
    print(mountains[1][1])


if __name__ == "__main__":
    main()
