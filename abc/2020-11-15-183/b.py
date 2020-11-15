def main():
    sx, sy, gx, gy = [int(x) for x in input().split()]
    ratio = gy / sy
    result = sx + (gx - sx) / (1.0 + ratio)
    print(result) 

if __name__ == "__main__":
    main()