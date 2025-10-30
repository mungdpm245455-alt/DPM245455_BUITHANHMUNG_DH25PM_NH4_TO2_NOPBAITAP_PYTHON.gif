#Câu 9: Xử lý mảng
'''
Yêu cầu:
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố.
M[] ={3,6,7,8,11,17,2,90,2,5,4,5,8}
➔ 3, 7, 11,17, 5(2) ➔6 số lẻ
'''

# Danh sách ban đầu
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# --- Hàm kiểm tra số nguyên tố ---
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Phân loại ---
so_le = [x for x in M if x % 2 != 0]
so_chan = [x for x in M if x % 2 == 0]
so_nguyen_to = [x for x in M if CheckPrime(x)]
khong_nguyen_to = [x for x in M if not CheckPrime(x)]

# --- Xuất kết quả ---
print("Dòng 1 - Các số lẻ:", so_le)
print("→ Có tổng cộng", len(so_le), "số lẻ.\n")

print("Dòng 2 - Các số chẵn:", so_chan)
print("→ Có tổng cộng", len(so_chan), "số chẵn.\n")

print("Dòng 3 - Các số nguyên tố:", so_nguyen_to)
print("→ Có tổng cộng", len(so_nguyen_to), "số nguyên tố.\n")

print("Dòng 4 - Các số không phải là số nguyên tố:", khong_nguyen_to)
print("→ Có tổng cộng", len(khong_nguyen_to), "số không nguyên tố.")

