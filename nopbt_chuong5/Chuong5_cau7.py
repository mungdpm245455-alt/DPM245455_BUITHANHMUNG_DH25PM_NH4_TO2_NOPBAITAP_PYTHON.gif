#Câu 7: Tối ưu chuỗi danh từ
'''
Yêu cầu:
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “ TRần duY thAnH ”
Output “Trần Duy Thanh”
'''
def ToiUuChuoiDanhTu(s):
    s = s.strip()            # Xóa khoảng trắng đầu và cuối
    arr = s.split()          # Tự động tách theo khoảng trắng (bỏ luôn khoảng trắng thừa)
    ket_qua = ""

    for tu in arr:
        tu = tu.lower()      # Đưa toàn bộ về chữ thường
        tu = tu.capitalize() # Viết hoa chữ cái đầu
        ket_qua += tu + " "

    return ket_qua.strip()   # Xóa khoảng trắng dư ở cuối

# --- Chương trình chính ---
s = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu:", ToiUuChuoiDanhTu(s))

