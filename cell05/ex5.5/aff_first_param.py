import sys

def main():
    # ตรวจสอบว่ามีพารามิเตอร์หรือไม่
    if len(sys.argv) > 1:
        # แสดงพารามิเตอร์แรกที่ส่งเข้ามา
        print(sys.argv[-5])
    else:
        # ถ้าไม่มีพารามิเตอร์ให้แสดง "none"
        print("none")

if __name__ == "__main__":
    main()
