import itertools

def eval(values):
    evaluated = set()
    for v in values:
        val = int(''.join([str(x) for x in v]))
        if val in evaluated:
            continue
        evaluated.add(val)
        if val % 8 == 0:
            return True
    return False

def get_numbers(s):
    """ Delete redundant numbers to generate the final 3 digits
    """
    ret = []
    for x in range(1, 10):
        count = s.count(x)
        if count > 3:
            count = 3
        for i in range(count):
            ret.append(x)
    return ret

def main():
    s = [int(c) for c in input()]
    s = get_numbers(s)
    
    result = False
    if len(s) < 3:
        result = eval(itertools.permutations(s))
    else:
        result = eval(itertools.permutations(s, 3))  # Generate final 3 digits
    
    if result:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()