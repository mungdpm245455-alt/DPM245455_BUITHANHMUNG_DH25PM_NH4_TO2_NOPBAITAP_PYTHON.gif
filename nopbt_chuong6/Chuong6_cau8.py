#Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.

# Nhập số phần tử
n = int(input("Nhập số phần tử n: "))

# Nhập dãy số thực
M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)

print("\nDãy số ban đầu:")
print(M)

# Sắp xếp giảm dần
M.sort(reverse=True)

print("\n✅ Dãy số sau khi sắp xếp giảm dần:")
print(M)