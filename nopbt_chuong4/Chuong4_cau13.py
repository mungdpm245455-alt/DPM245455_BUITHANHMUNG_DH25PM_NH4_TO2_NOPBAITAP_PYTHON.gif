#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
'''
Yêu cầu:
Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
a) Kiểm tra số nguyên dương n có phải là số hoàn thiện (Pefect number) hay không?
(Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó.
Vd: 6 có các ước số là 1,2,3 và 6=1+2+3 ➔6 là số hoàn thiện)
b) Kiểm tra số nguyên dương n có phải là số thịnh vượng (Abundant number)hay
không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn
nó. Vd:12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 ➔12 là số thịnh vượng)
'''
def tong_uoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def la_so_hoan_thien(n):
    return tong_uoc(n) == n

def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

# --- Chạy thử ---
n = int(input("Nhập số nguyên dương n: "))

if la_so_hoan_thien(n):
    print(n, "là số hoàn thiện (Perfect Number)")
elif la_so_thinh_vuong(n):
    print(n, "là số thịnh vượng (Abundant Number)")
else:
    print(n, "không phải số hoàn thiện hay thịnh vượng")
