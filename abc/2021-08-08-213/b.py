def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    players = [(i + 1, x) for i, x in enumerate(A)]
    players.sort(key=lambda x: x[1], reverse=True)
    print(players[1][0])


if __name__ == "__main__":
    main()
