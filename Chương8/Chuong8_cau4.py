#Câu 4: Phần mềm máy tính bỏ túi
'''
Yêu cầu:
Thiết kế Calculator đơn giản
Phần mềm cho người sử dụng làm các phép toán cơ bản: +, - , *, / và xóa toàn bộ
phần mềm.
'''
import tkinter as tk

# Hàm xử lý khi người dùng nhấn nút
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Lỗi")
    elif text == "Clr":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.geometry("250x300")

# Khung hiển thị
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 16 bold", justify='right')
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Danh sách các nút theo từng hàng
button_rows = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["+", "0", "-"],
    ["*", "/", "="],
    ["Clr"]
]

# Tạo và bố trí nút
for row in button_rows:
    frame = tk.Frame(root)
    frame.pack()
    for text in row:
        button = tk.Button(frame, text=text, font="Arial 14", width=5, height=2)
        button.pack(side=tk.LEFT, padx=2, pady=2)
        button.bind("<Button-1>", click)

# Chạy chương trình
root.mainloop()