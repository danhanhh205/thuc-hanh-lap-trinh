print("Sinh vien:Nguyễn Danh Ánh")
print("Mssv:235752021610023")
n = int(input("Nhập số nguyên n: "))
def fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
fib_list = fibonacci_list(n)
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fib_list)
