#Câu 5: Màn hình đăng nhập
'''
Yêu cầu:
Thiết kế màn hình đăng nhập:
'''
import tkinter as tk
from tkinter import messagebox

def submit():
    old = old_pass.get()
    new = new_pass.get()
    confirm = confirm_pass.get()
    if not old or not new or not confirm:
        messagebox.showwarning("Thông báo", "Vui lòng nhập đầy đủ thông tin!")
    elif new != confirm:
        messagebox.showerror("Lỗi", "Mật khẩu mới không trùng khớp!")
    else:
        messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")

def cancel():
    root.destroy()

# Cửa sổ chính
root = tk.Tk()
root.title("Enter New Password")
root.geometry("350x180")
root.resizable(False, False)

# Giao diện nhập liệu
tk.Label(root, text="Old Password:").place(x=20, y=20)
tk.Label(root, text="New Password:").place(x=20, y=60)
tk.Label(root, text="Enter New Password Again:").place(x=20, y=100)

old_pass = tk.Entry(root, show="*", width=25)
new_pass = tk.Entry(root, show="*", width=25)
confirm_pass = tk.Entry(root, show="*", width=25)

old_pass.place(x=180, y=20)
new_pass.place(x=180, y=60)
confirm_pass.place(x=180, y=100)

# Nút lệnh
tk.Button(root, text="OK", width=10, command=submit).place(x=100, y=135)
tk.Button(root, text="Cancel", width=10, command=cancel).place(x=200, y=135)

root.mainloop()