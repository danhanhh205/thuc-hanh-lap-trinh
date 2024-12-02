print("Nguyễn Danh Ánh")
print("235752021610023")

import tkinter as tk

def thay_doi_mau():
    button.config(bg="green", fg="white")

window = tk.Tk()
window.title("Thay đổi màu nút")

button = tk.Button(window, text="Nhấn vào đây", command=thay_doi_mau)
button.pack()

window.mainloop()
