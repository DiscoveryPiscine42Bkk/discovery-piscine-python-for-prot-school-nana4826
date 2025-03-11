# multiplication_table.py

def main():
    # รับค่าตัวเลขจากผู้ใช้
    number = int(("2"))
    
    # แสดงตารางการคูณจาก 1 ถึง 12
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    main()
