import heapq

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]

    q = [(t, n, s) for n, s, t in zip(range(0, N), S, T)]
    heapq.heapify(q)
    
    ans = {}
    while len(ans) < N:
        t, n, s = heapq.heappop(q)
        if n not in ans:
            ans[n] = t
        next_n = (n + 1) % N
        heapq.heappush(q, (t + s, next_n, S[next_n]))
        
    for i in range(0, N):
        print(ans[i])


if __name__ == "__main__":
    main()
