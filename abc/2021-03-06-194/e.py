from collections import defaultdict


def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    pos = defaultdict(lambda: [-1])  # key = value of A, value = list of indices having the key value
    for i, a in enumerate(A):
        pos[a].append(i)
    for a in range(0, N):
        indices = pos[a]
        if len(indices) == 1 and indices[0] == -1:
            # value a does not exist in A, so this will be the minimum mex
            print(a)
            return
        indices.append(N)
        for i, index in enumerate(indices):
            if i + 1 < len(indices) and indices[i + 1] - index > M:
                # A has a sub-array longer than M having no value of a, 
                # so the value of a will be the minimum mex
                print(a)
                return
    print(a + 1)


if __name__ == "__main__":
    main()
