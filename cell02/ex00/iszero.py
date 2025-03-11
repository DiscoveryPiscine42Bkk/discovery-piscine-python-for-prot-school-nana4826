#!/usr/bin/env python3

def main():
    try:
        number = float(input("0"))
        if number == 0:
            print("ตัวเลขนี้เท่ากับศูนย์")
        else:
            print("ตัวเลขนี้ต่างจากศูนย์")
    except ValueError:
        print("0,1,2,3,4")

if __name__ == "__main__":
    main()
