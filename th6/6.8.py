print('sinh vien: Nguyễn Danh Ánh')
print('mssv:235752021610023')
print('##########')
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Số dư hiện tại của bạn là: {self.balance} VNĐ")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Bạn đã gửi {amount} VNĐ. Số dư mới là: {self.balance} VNĐ")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Số dư không đủ để rút số tiền này.")
        elif amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        else:
            self.balance -= amount
            print(f"Bạn đã rút {amount} VNĐ. Số dư mới là: {self.balance} VNĐ")


def main():
    atm = ATM() 
    while True:
        print("\nChọn giao dịch:")
        print("1. Kiểm tra số dư")
        print("2. Gửi tiền")
        print("3. Rút tiền")
        print("4. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Nhập số tiền bạn muốn gửi: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Nhập số tiền bạn muốn rút: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
