print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
numbers = input("Nhập các số, phân tách bằng dấu phẩy: ").split(',')
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]
print(",".join(map(str, odd_numbers)))
