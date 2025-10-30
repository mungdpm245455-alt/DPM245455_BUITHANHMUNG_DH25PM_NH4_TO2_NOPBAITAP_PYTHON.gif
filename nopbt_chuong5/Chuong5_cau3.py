#Câu 3: Xử lý Tách chuỗi
'''
Yêu cầu:
Cho 1 Chuỗi như sau “5;7;8;-2;8;11;13;9;10” (có thể nhập bất kỳ từ bàn phím)
- xuất các chữ số trên các dòng riêng biệt
- Xuất có bao nhiêu chữ số chẵn
- Xuất có bao nhiêu số âm
- Xuất có bao nhiêu chữ số nguyên tố
- Tính giá trị trung bình
'''
def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(';')

sochan = 0
soam = 0
sont = 0
tong = 0

for x in arr:
    number = int(x)
    print(number)
    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        sont += 1
    tong += number

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
