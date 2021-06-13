# https://qiita.com/gogotealove/items/11f9e83218926211083a


def get_purchase_patterns(money, items):
    ret = []
    n = len(items)
    for i in range(2 ** n):
        # for each pattern
        bag = []
        price = 0
        for j in range(n):
            # for each bit (each item)
            if (i >> j) & 1:
                # if jth bit of i is 1
                item = items[j]
                bag.append(item[0])
                price += item[1]
        if price <= money:
            ret.append(bag)
    return ret


if __name__ == "__main__":
    money = 300
    items = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
    print(get_purchase_patterns(money, items))
