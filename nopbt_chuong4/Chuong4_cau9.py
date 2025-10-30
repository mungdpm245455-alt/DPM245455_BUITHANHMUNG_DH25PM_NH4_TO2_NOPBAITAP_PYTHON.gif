#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau
'''
'''
import math

print("Chương trình tính căn bậc 2 lồng nhau")

n = int(input("Nhập n (số dấu căn): "))

s = 0
for i in range(n):
    s = math.sqrt(2 + s)

print(f"S({n}) = {s}")
