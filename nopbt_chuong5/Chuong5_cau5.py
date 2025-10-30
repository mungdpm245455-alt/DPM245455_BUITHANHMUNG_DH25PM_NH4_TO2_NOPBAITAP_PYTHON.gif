#Câu 5: Xử lý chuỗi với các hàm cơ bản
'''
Yêu cầu:
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm

                         
'''
def XuLyChuoi(s):
    so_in_hoa = 0
    so_in_thuong = 0
    so_chu_so = 0
    so_ky_tu_dac_biet = 0
    so_khoang_trang = 0
    so_nguyen_am = 0
    so_phu_am = 0

    nguyen_am = "aeiouAEIOU"   # Các nguyên âm

    for ch in s:
        if ch.isupper():
            so_in_hoa += 1
        elif ch.islower():
            so_in_thuong += 1

        if ch.isdigit():
            so_chu_so += 1
        elif not ch.isalnum() and not ch.isspace():
            so_ky_tu_dac_biet += 1
        elif ch.isspace():
            so_khoang_trang += 1

        # Đếm nguyên âm và phụ âm (chỉ áp dụng cho chữ cái)
        if ch.isalpha():
            if ch in nguyen_am:
                so_nguyen_am += 1
            else:
                so_phu_am += 1

    # In kết quả
    print("Số chữ IN HOA:", so_in_hoa)
    print("Số chữ in thường:", so_in_thuong)
    print("Số chữ là chữ số:", so_chu_so)
    print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)
    print("Số khoảng trắng:", so_khoang_trang)
    print("Số nguyên âm:", so_nguyen_am)
    print("Số phụ âm:", so_phu_am)


# --- Chương trình chính ---
s = input("Nhập một chuỗi bất kỳ: ")
XuLyChuoi(s)
