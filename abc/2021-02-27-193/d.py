from itertools import permutations


def get_cards(input_str, cards):
    ret = [0 for _ in range(10)]
    for s in input_str:
        s = int(s)
        cards[s] -= 1
        ret[s] += 1
    return ret


def get_possible_cards(cards):
    ret = []
    for i, x in enumerate(cards):
        if i == 0:
            continue
        if x >= 1:
            ret.append(i)
        if x >= 2:
            ret.append(i)
    return ret


def main():
    K = int(input())
    S = input()
    T = input()
    cards = [K for _ in range(10)]
    s_cards = get_cards(S[:4], cards)
    t_cards = get_cards(T[:4], cards)
    possible_cards = get_possible_cards(cards)
    cards_sum = sum([x for x in cards[1:]])
    ans = 0.0
    memo = set()
    for s, t in permutations(possible_cards, 2):
        key = str(s) + str(t)
        if key in memo:
            continue
        memo.add(key)
        s_cards[s] += 1
        t_cards[t] += 1
        s_score = sum([i * (10 ** x) for i, x in enumerate(s_cards)])
        t_score = sum([i * (10 ** x) for i, x in enumerate(t_cards)])
        if s_score > t_score:
            # print(f"s={s}, t={t}, s_score={s_score}, t_score={t_score}")
            x = cards[t] - 1 if s == t else cards[t]
            ans += (cards[s] * x * (10 ** 5)) / cards_sum / (cards_sum - 1) / 10 ** 5
        s_cards[s] -= 1
        t_cards[t] -= 1
    print(ans)


if __name__ == "__main__":
    main()
