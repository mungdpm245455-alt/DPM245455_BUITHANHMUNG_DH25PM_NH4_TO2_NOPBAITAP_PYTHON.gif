#Câu 3: Xử lý List Đa chiều
'''
Yêu cầu:
Viết chương trình cho phép:
- Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên
- Xuất dòng bất kỳ nhập từ bàn phím
- Xuất cột bất kỳ từ bàn phím
- Xuất số MAX trong ma trận
'''
from random import randrange

# Hàm tạo ma trận ngẫu nhiên
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

# Hàm xuất ma trận
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# Lấy dòng r
def LayDong(D, r):
    return D[r]

# Xuất list 1 chiều
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# Lấy cột c
def LayCot(D, c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

# Tìm phần tử lớn nhất trong ma trận
def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val


# ======== CHƯƠNG TRÌNH CHÍNH ========
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)

print("Ma trận ngẫu nhiên là:")
XuatMaTran(D)

# Xuất dòng
r = int(input("Mời bạn nhập dòng muốn xuất: "))
print("Dòng", r, ":")
XuatList1Chieu(LayDong(D, r))

# Xuất cột
c = int(input("Mời bạn nhập cột muốn xuất: "))
print("Cột", c, ":")
XuatList1Chieu(LayCot(D, c))

# Tìm giá trị lớn nhất
max_val = MAX(D)
print("Số lớn nhất trong ma trận =", max_val)
