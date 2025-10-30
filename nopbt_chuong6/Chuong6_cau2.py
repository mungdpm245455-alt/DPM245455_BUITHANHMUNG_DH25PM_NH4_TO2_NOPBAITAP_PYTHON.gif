#Câu 2: Xử lý List nhập ngẫu nhiên
'''
Yêu cầu:
Viết chương trình cho phép:
- Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list
- Gọi k là một số nhập từ bàn phím, hãy xóa tất cả các phần tử có giá trị k tồn tại
trong list
- Kiểm tra list có đối xứng hay không
'''
from random import randrange

lst = []

# Nhập số phần tử
n = int(input("Nhập số phần tử: "))

# Tạo list ngẫu nhiên
for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# Chèn thêm số mới
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# Xóa tất cả các phần tử có giá trị k
k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)

print("List sau khi xóa:")
print(lst)

# Hàm kiểm tra list đối xứng
def CheckDoiXung(lst):
    for i in range(len(lst) // 2):  # chỉ cần kiểm tra nửa đầu
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

# Gọi hàm kiểm tra đối xứng
if CheckDoiXung(lst):
    print("List đối xứng")
else:
    print("List không đối xứng")
