print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
def benefit(t, n, k):
    t_decimal = t / 100
    total_amount = n * (1 + t_decimal) ** k
    return round(total_amount, 2)
try:
    t = float(input("Nhập lãi suất (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    print(f"Số tiền nhận được sau {k} tháng: {benefit(t, n, k)}")
except ValueError:
    print("Vui lòng nhập các giá trị hợp lệ.")
