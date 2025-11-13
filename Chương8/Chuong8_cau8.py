#Câu 8: Thiết kế màn hình chuyển độ F thành độ C
'''
Yêu cầu:
Thiết kế màn hình chuyển độ F thành độ C
'''
import tkinter as tk
from tkinter import messagebox

# Hàm chuyển đổi
def chuyen_doi():
    try:
        doF = float(entry_F.get())
        doC = (doF - 32) * 5 / 9
        label_kq.config(text=f"{doC:.2f} °C")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Giao diện chính
root = tk.Tk()
root.title("Chuyển đổi độ F sang độ C")
root.configure(bg="yellow")

# Nhãn và ô nhập
tk.Label(root, text="Nhập độ F:", bg="yellow").grid(row=0, column=0, padx=10, pady=10)
entry_F = tk.Entry(root, width=10, fg="red", justify="center")
entry_F.grid(row=0, column=1, padx=10, pady=10)
entry_F.insert(0, "350")  # Giá trị mẫu

# Nút "Chuyển"
btn = tk.Button(root, text="Chuyển", command=chuyen_doi, bg="#4287f5", fg="white")
btn.grid(row=1, column=1, pady=10)

# Kết quả
tk.Label(root, text="Độ C:", bg="yellow").grid(row=2, column=0, padx=10, pady=10)
label_kq = tk.Label(root, text="Độ C ở đây", bg="yellow", fg="black")
label_kq.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()