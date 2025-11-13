#Câu 9: Phần mềm tính BMI
'''
Yêu cầu:
Thiết kế màn hình tính BMI như hình dưới đây
Viết chương trình tính chỉ số BMI của một người khi biết chiều cao và cân nặng. Biết rằng:
BMI = Weight / (Height*Height)
Cho biết tình trạng cân nặng của người này dựa trên tiêu chuẩn quốc tế 
'''
import tkinter as tk
from tkinter import messagebox

def tinh_BMI():
    try:
        cao = float(entry_cao.get())
        nang = float(entry_nang.get())
        bmi = nang / (cao * cao)
        entry_bmi.delete(0, tk.END)
        entry_bmi.insert(0, f"{bmi:.2f}")

        # Xác định tình trạng và nguy cơ
        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif bmi < 23:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif bmi < 25:
            tinh_trang = "Hơi béo"
            nguy_co = "Hơi cao"
        elif bmi < 30:
            tinh_trang = "Béo phì độ I"
            nguy_co = "Cao"
        else:
            tinh_trang = "Béo phì độ II"
            nguy_co = "Rất cao"

        entry_tinhtrang.delete(0, tk.END)
        entry_tinhtrang.insert(0, tinh_trang)

        entry_nguyco.delete(0, tk.END)
        entry_nguyco.insert(0, nguy_co)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Thoát chương trình
def thoat():
    root.destroy()

# Cửa sổ chính
root = tk.Tk()
root.title("Tính chỉ số BMI")
root.configure(bg="yellow")

# Giao diện
tk.Label(root, text="Nhập chiều cao (m):", bg="yellow").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_cao = tk.Entry(root, fg="red", justify="center")
entry_cao.grid(row=0, column=1, pady=5)
entry_cao.insert(0, "1.8")

tk.Label(root, text="Nhập cân nặng (kg):", bg="yellow").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_nang = tk.Entry(root, fg="red", justify="center")
entry_nang.grid(row=1, column=1, pady=5)
entry_nang.insert(0, "72")

btn_tinh = tk.Button(root, text="Tính BMI", bg="#4287f5", fg="white", command=tinh_BMI)
btn_tinh.grid(row=2, column=1, pady=10)

tk.Label(root, text="BMI của bạn:", bg="yellow").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_bmi = tk.Entry(root, justify="center")
entry_bmi.grid(row=3, column=1, pady=5)

tk.Label(root, text="Tình trạng của bạn:", bg="yellow").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_tinhtrang = tk.Entry(root, justify="center", fg="red")
entry_tinhtrang.grid(row=4, column=1, pady=5)

tk.Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_nguyco = tk.Entry(root, justify="center", fg="red")
entry_nguyco.grid(row=5, column=1, pady=5)

btn_thoat = tk.Button(root, text="Thoát", bg="#4287f5", fg="white", command=thoat)
btn_thoat.grid(row=6, column=1, pady=10)

root.mainloop()