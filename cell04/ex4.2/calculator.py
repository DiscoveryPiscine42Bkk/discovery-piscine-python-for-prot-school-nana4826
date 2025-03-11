# calculator.py

# ขอให้ผู้ใช้ป้อนตัวเลขสองตัว
Z = float(input("ป้อนตัวเลขตัวแรก: "))
A = float(input("ป้อนตัวเลขตัวที่สอง: "))

# คำนวณและแสดงผลลัพธ์ของการบวก ลบ หาร และคูณ
sum_result = Z + A
diff_result = Z- A
prod_result = Z * A
if A != 0:
    div_result = Z / A
else:
    div_result = "ไม่สามารถหารด้วย 0 ได้"

# แสดงผลลัพธ์
print(f"ผลบวกของ {Z} + {A} = {sum_result}")
print(f"ผลลบของ {Z} - {A} = {diff_result}")
print(f"ผลคูณของ {Z} * {A} = {prod_result}")
print(f"ผลหารของ {Z} / {A} = {div_result}")
