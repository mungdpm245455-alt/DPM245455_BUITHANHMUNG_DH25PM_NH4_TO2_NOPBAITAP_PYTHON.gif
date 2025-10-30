#Câu 10: Xử lý Ma Trận
'''
Yêu cầu:
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B
'''
# --- Hàm nhập ma trận ---
def NhapMaTran(ten):
    m = int(input(f"Nhập số dòng của ma trận {ten}: "))
    n = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}] = "))
            row.append(x)
        M.append(row)
    return M

# --- Hàm xuất ma trận ---
def XuatMaTran(M, ten="Ma trận"):
    print(f"\n{ten}:")
    for row in M:
        for val in row:
            print(val, end='\t')
        print()

# --- Hàm cộng hai ma trận ---
def CongMaTran(A, B):
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# --- Hàm hoán vị ma trận ---
def HoanVi(M):
    m, n = len(M), len(M[0])
    HT = []
    for j in range(n):
        row = []
        for i in range(m):
            row.append(M[i][j])
        HT.append(row)
    return HT


# =============================
# Chương trình chính
# =============================

print("=== NHẬP MA TRẬN A ===")
A = NhapMaTran("A")

print("\n=== NHẬP MA TRẬN B ===")
B = NhapMaTran("B")

# Kiểm tra kích thước trước khi cộng
if len(A) == len(B) and len(A[0]) == len(B[0]):
    C = CongMaTran(A, B)
    XuatMaTran(A, "Ma trận A")
    XuatMaTran(B, "Ma trận B")
    XuatMaTran(C, "Tổng ma trận C = A + B")
else:
    print("\n Hai ma trận không cùng kích thước, không thể cộng!")

# Hoán vị ma trận
A_T = HoanVi(A)
B_T = HoanVi(B)
XuatMaTran(A_T, "Hoán vị của A (Aᵀ)")
XuatMaTran(B_T, "Hoán vị của B (Bᵀ)")


