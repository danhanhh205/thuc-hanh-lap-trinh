print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:

    if b == 0:
        print("Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm")
    else:
        print(f"Phương trình có nghiệm duy nhất: x = {-c / b}")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép: x = {-b / (2 * a)}")
    else:
        print("Phương trình vô nghiệm")

