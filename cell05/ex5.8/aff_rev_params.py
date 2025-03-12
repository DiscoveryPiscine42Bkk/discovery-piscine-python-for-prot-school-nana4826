import sys

def main():
    if len(sys.argv) > 2:  # ตรวจสอบว่ามีอาร์กิวเมนต์พอหรือไม่
        print(sys.argv[2])  # พิมพ์ค่าของ argument ที่สาม
    else:
        print("none")

if __name__ == "__main__":
    main()
