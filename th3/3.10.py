print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
import math
def Tinh(R):
    if R <= 0:
        return "Bán kính không hợp lệ, vui lòng nhập giá trị lớn hơn 0."
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    return f"Chu vi hình tròn là: {chu_vi:.2f}, Diện tích hình tròn là: {dien_tich:.2f}"
try:
    R = float(input("Nhập bán kính hình tròn: "))
    print(Tinh(R))
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
