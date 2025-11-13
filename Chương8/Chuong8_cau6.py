#Câu 6: Màn hình cấu hình Style cho Button
'''
Yêu cầu:
Viết code hiển thị các loại style của Button trong Python
'''
import tkinter as tk

root = tk.Tk()
root.title("frame 2")

# Danh sách các kiểu relief của Button
reliefs = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

# Tạo nhãn tiêu đề
tk.Label(root, text="borderwidth = 0").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="borderwidth = 1").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="borderwidth = 2").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="borderwidth = 3").grid(row=3, column=0, padx=5, pady=5)
tk.Label(root, text="borderwidth = 4").grid(row=4, column=0, padx=5, pady=5)

# Hiển thị các kiểu nút tương ứng
for i, bw in enumerate(range(0, 5)):
    for j, relief in enumerate(reliefs):
        btn = tk.Button(root, text=relief, relief=relief, borderwidth=bw, width=8)
        btn.grid(row=i, column=j + 1, padx=5, pady=5)

root.mainloop()