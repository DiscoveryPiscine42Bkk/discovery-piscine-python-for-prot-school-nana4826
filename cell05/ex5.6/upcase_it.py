import sys

def main():
    # ตรวจสอบว่ามีพารามิเตอร์เพียงแค่ 1 ตัวหรือไม่
    if len(sys.argv) == 2:
        # แสดงสตริงที่รับเข้ามาในรูปตัวพิมพ์ใหญ่
        print(sys.argv[1].upper())
    else:
        # ถ้ามีพารามิเตอร์ไม่เท่ากับ 1 ให้แสดง "none"
        print("none")

if __name__ == "__main__":
    main()
