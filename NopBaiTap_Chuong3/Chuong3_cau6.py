#Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ. (vd: n=35 => Ba mươi lăm, n=5 => năm)
'''
'''
def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", 
                 "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ. Vui lòng nhập số từ 0 đến 99."

    if n < 10:
        
        if n == 5:
            return "năm"
        elif n == 0:
            return "không"
        else:
            return don_vi[n]

    chuc = n // 10
    dv = n % 10

    ket_qua = hang_chuc[chuc]

    if dv == 0:
        return ket_qua
    elif dv == 1:
        if chuc == 1:
            ket_qua += " một"
        else:
            ket_qua += " mốt"
    elif dv == 5:
        ket_qua += " lăm"
    else:
        ket_qua += " " + don_vi[dv]

    return ket_qua.capitalize()



n = int(input("Nhập số nguyên (0-99): "))
print("Cách đọc:", doc_so(n))

