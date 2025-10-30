#Câu 8: Viết chương trình tính logax
'''
Yêu cầu:
Viết chương trình tính logax với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
!= 1.( dùng logax=lnx/lna)
'''
import math

print("Chương trình tính log_a(x)")

# Nhập giá trị a và x
a = float(input("Nhập cơ số a (a > 0, a ≠ 1): "))
x = float(input("Nhập số x (x > 0): "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
else:
    print("Dữ liệu không hợp lệ! (yêu cầu a > 0, a ≠ 1, x > 0)")
