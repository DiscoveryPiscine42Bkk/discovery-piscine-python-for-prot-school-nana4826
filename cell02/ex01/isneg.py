#!/usr/bin/env python3

def main():
    try:
        number = float(input("0,-1,-2,1,2"))
        if number < 0:
            print("ตัวเลขนี้เป็นลบ")
        elif number > 0:
            print("ตัวเลขนี้เป็นบวก")
        else:
            print("ตัวเลขนี้เป็นทั้งบวกและลบ")
    except ValueError:
        print("0,-1,-2,1,2")

if __name__ == "__main__":
    main()
