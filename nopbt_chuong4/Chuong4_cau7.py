#Câu 7: Tính và xuất độ dài đoạn AB
'''
Yêu cầu:
Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB.
'''
from math import sqrt

print("Chương trình tính độ dài đoạn thẳng AB")

# Nhập tọa độ 2 điểm
xa = float(input("Nhập hoành độ xA: "))
ya = float(input("Nhập tung độ yA: "))
xb = float(input("Nhập hoành độ xB: "))
yb = float(input("Nhập tung độ yB: "))

# Tính độ dài đoạn AB
dAB = sqrt((xb - xa)**2 + (yb - ya)**2)

# Xuất kết quả
print("Độ dài đoạn AB =", dAB)
