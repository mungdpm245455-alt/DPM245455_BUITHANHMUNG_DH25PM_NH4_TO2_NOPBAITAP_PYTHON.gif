#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

import random

n = int(input("Nhập số phần tử N: "))

# Tạo list gồm N số ngẫu nhiên KHÔNG TRÙNG NHAU trong khoảng 0–99
lst = random.sample(range(100), n)

print("List ngẫu nhiên không trùng là:")
print(lst)
