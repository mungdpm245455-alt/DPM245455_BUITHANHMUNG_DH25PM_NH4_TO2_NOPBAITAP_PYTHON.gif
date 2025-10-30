#Câu 1: Xử lý List
'''
Yêu cầu:
Viết chương trình cho phép:
- Khởi tạo list
- Thêm phần tử vào list
- Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list
- Tính tổng các số nguyên tố trong list
- Sắp xếp
- Xóa list
'''
from random import randrange

print("Chương trình xử lý List")

# Nhập số phần tử
n = int(input("Nhập số phần tử: "))

# Tạo list ngẫu nhiên
lst = [randrange(-100, 100) for _ in range(n)]
print("List ngẫu nhiên là:")
print(lst)

# Thêm phần tử mới
value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm:")
print(lst)

# Đếm số xuất hiện
k = int(input("Bạn muốn đếm số nào: "))
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list.")

# Hàm kiểm tra số nguyên tố
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đếm và tính tổng các số nguyên tố
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list.")
print("Tổng các số nguyên tố =", tongnt)

# Sắp xếp list
lst.sort()
print("List sau khi sort:")
print(lst)

# Xóa list
lst.clear()
print("List sau khi xóa:")
print(lst)