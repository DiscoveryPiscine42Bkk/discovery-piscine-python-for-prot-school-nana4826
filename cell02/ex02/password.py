password = "Python is awesome"

# ขอให้ผู้ใช้ป้อนรหัสผ่าน
user_input = input("Enter the password: ")

# ตรวจสอบว่ารหัสผ่านถูกต้องหรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")