def main():
    N, W = [int(x) for x in input().split()]
    water_plan = [0 for x in range(0, 2 * 100000)]
    can_serve = True
    for n in range(0, N):
        S, T, P = [int(x) for x in input().split()]
        if not can_serve:
            # No need to update the plan
            continue
        for i in range(S, T):
            water_plan[i] += P
            if water_plan[i] > W:
                can_serve = False
                break
    print("Yes" if can_serve else "No")
 
 
if __name__ == "__main__":
    main()