print("Nguyễn Danh Ánh")
print("235752021610023")
import tkinter as tk

def nhan_phim(event):
    print("Bạn đã nhấn phím:", event.char)

window = tk.Tk()
window.title("Xử lý sự kiện phím bấm")

frame = tk.Frame(window)
frame.pack()

frame.bind("<Key>", nhan_phim)

window.mainloop()
