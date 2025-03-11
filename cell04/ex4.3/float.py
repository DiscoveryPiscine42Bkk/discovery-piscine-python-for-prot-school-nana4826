# calculator.py


n = float(input("ป้อนตัวเลขตัวแรก: "))
s = float(input("ป้อนตัวเลขตัวที่สอง: "))

sum_result = n + s
diff_result = n - s
prod_result = n * s
if s != 0:
    div_result = n / s
else:
    div_result = "ไม่สามารถหารด้วย 0 ได้"

print(f"ผลบวกของ {n} + {s} = {sum_result}")
print(f"ผลลบของ {n} - {s} = {diff_result}")
print(f"ผลคูณของ {n} * {s} = {prod_result}")
print(f"ผลหารของ {n} / {s} = {div_result}")
