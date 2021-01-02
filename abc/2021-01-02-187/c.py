def main():
    N = int(input())
    S = set()
    satisfiable = True
    example = None
    for i in range(N):
        s = input()
        not_example = False
        if s.startswith("!"):
            not_example = True
        if not_example and s[1:] in S:
            satisfiable = False
            example = s[1:]
        elif not not_example and "!" + s in S:
            satisfiable = False
            example = s
        S.add(s)
    if not satisfiable:
        print(example)
    else:
        print("satisfiable")


if __name__ == "__main__":
    main()
