def main():
    num = int(float(input()) * 10)
    X = num // 10
    Y = num % 10
    if 0 <= Y and Y <= 2:
        print(f"{X}-")
    elif 3 <= Y and Y <= 6:
        print(f"{X}")
    else:
        print(f"{X}+")
    

if __name__ == "__main__":
    main()
