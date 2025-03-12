import sys

def main():
    if len(sys.argv) != 2:
        print("ไม่มี")
        return

    parameter = sys.argv[1]
    user_input = input("ป้อนคำ: ")

    if user_input == parameter:
        print("ทำได้ดี!")
    else:
        print("ไม่ล่ะ ขอโทษ...")

if __name__ == "__main__":
    main()
