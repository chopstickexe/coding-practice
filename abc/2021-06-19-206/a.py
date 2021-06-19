import math

def main():
    N = int(input())
    x = math.floor(1.08 * N) 
    if x < 206:
        print("Yay!")
    elif x == 206:
        print("so-so")
    else:
        print(":(") 


if __name__ == "__main__":
    main()
